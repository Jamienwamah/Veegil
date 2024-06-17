import React, { useState, useEffect } from "react";
import axios from 'axios';
import jwt_decode from 'jwt-decode';
import { useRouter } from 'next/router';
import { useMutation } from '@apollo/client';
import { RiExchangeDollarLine } from 'react-icons/ri';
import { CREATEDEPOSIT } from '../components/graphql/mutations';
import clients from '../components/apollo/client';

const DepositForm = () => {
  // State Management
  const [user, setUser] = useState('');
  const [accountNumber, setAccountNumber] = useState('');
  const [amount, setAmount] = useState('');
  const [error, setError] = useState(null);
  
  // Router
  const router = useRouter();

  // Apollo Client
  const [createDeposit] = useMutation(CREATEDEPOSIT, {
    client: clients.deposit,
    onError: (error) => {
      console.error('Error depositing funds (GraphQL):', error.message);
      setError(error.message);
    },
    onCompleted: () => {
      console.log('Deposit successful (GraphQL)');
      // Reset form fields after successful deposit
      setUser('');
      setAccountNumber('');
      setAmount('');
    },
  });

  // Effects
  useEffect(() => {
    // Check if the user is authenticated
    const token = localStorage.getItem('token');
    if (!token) {
      // If the token is not present, redirect the user to the login page
      router.push('/login');
    } else {
      // Decode token to get user information
      const decoded = jwt_decode(token);
      setUser(decoded.username);
    }
  }, []);

  // Event Handlers
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Get token from local storage
      const token = localStorage.getItem('token');

      // Decode token to get user information
      const decoded = jwt_decode(token);

      // Call Apollo mutation for deposit
      const result = await createDeposit({
        variables: {
          user: decoded.username,
          accountNumber,
          amount
        }
      });

      console.log('Deposit successful (GraphQL):', result.data);

    } catch (graphqlError) {
      console.error('Error depositing funds (GraphQL):', graphqlError);
      setError(graphqlError.message); // Set error message state

      // If GraphQL mutation fails, try depositing using REST API
      try {
        const token = localStorage.getItem('token');
        const decoded = jwt_decode(token);
        const response = await axios.post('https://bankapp-hd3c.onrender.com/api/v1/deposit/', {
          user: decoded.username,
          accountNumber,
          amount
        }, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        
        console.log('Deposit successful (REST):', response.data);
      } catch (restError) {
        console.error('Error depositing funds (REST):', restError);
        setError(restError.message);
      }
    }
  };

  // Form JSX
  return (
    <div className="flex items-center justify-center">
      <form onSubmit={handleSubmit} className="flex flex-col items-center z-10">
        <button type="submit">Deposit</button>
      </form>
      <RiExchangeDollarLine className="ml-4 z-10" size={40} />
    </div>
  );
};

export default DepositForm;
