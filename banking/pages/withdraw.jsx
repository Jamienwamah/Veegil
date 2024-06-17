import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { RiExchangeDollarLine } from 'react-icons/ri';
import jwt_decode from 'jwt-decode'; 
import { useRouter } from 'next/router';
import { useMutation } from '@apollo/client'; 
import { CREATEWITHDRAW } from '../components/graphql/mutations.js'; 
import clients from '../components/apollo/client.js'; 

const WithdrawForm = () => {
  const [user, setUser] = useState('');
  const [accountNumber, setAccountNumber] = useState('');
  const [amount, setAmount] = useState('');
  const [error, setError] = useState(null);
  const router = useRouter();

  useEffect(() => {
    
    const token = localStorage.getItem('token');
    if (!token) {
    
      router.push('/login');
    }
  }, [router]);

  
  const [withdrawFunds] = useMutation(CREATEWITHDRAW, {
    client: clients.transfer, 
    onError: (error) => {
      console.error('Error withdrawing funds (GraphQL):', error.message);
      setError(error.message);
    },
    onCompleted: () => {
      console.log('Withdrawal successful (GraphQL)');
      setUser('');
      setAccountNumber('');
      setAmount('');
    },
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Get token from local storage
      const token = localStorage.getItem('token');

      // Decode token to get user information
      const decoded = jwt_decode(token);

      // Call the withdrawFunds mutation with the necessary variables
      await withdrawFunds({
        variables: {
          user: decoded.username,
          accountNumber,
          amount: parseFloat(amount),
        },
      });

      // If the GraphQL mutation fails, fall back to the REST API request
      if (error) {
        const response = await axios.post('https://bankapp-hd3c.onrender.com/api/v1/withdraw/', {
          user: decoded.username,
          accountNumber,
          amount
        }, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        console.log('Withdrawal successful (REST):', response.data);
        setUser('');
        setAccountNumber('');
        setAmount('');
      }
    } catch (error) {
      console.error('Error withdrawing funds (REST):', error);
      setError(error.message);
    }
  };

  return (
    <div className="flex items-center justify-center">
      <form onSubmit={handleSubmit} className="flex flex-col items-center">
      </form>
      <RiExchangeDollarLine className="ml-4" size={40} />
    </div>
  );
};

export default WithdrawForm;
