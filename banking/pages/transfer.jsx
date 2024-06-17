import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { RiExchangeDollarLine } from 'react-icons/ri';
import jwt_decode from 'jwt-decode';
import { useRouter } from 'next/router';
import { useMutation } from '@apollo/client';
import { CREATETRANSFER } from '../components/graphql/mutations'; // Import GraphQL mutation
import clients from '../components/apollo/client'; // Import Apollo Client instance

const TransferForm = () => {
  // State variables
  const [sender, setSender] = useState('');
  const [receiver, setReceiver] = useState('');
  const [amount, setAmount] = useState('');
  const [error, setError] = useState(null);
  const router = useRouter();

  // Apollo Client mutation hook for transferring funds
  const [transferFunds] = useMutation(CREATETRANSFER, {
    client: clients.transfer,
    onError: (error) => {
      console.error('Error transferring funds (GraphQL):', error.message);
      setError(error.message);
    },
    onCompleted: () => {
      console.log('Transfer successful (GraphQL)');
      setSender('');
      setReceiver('');
      setAmount('');
    },
  });

  useEffect(() => {
    const checkAuthentication = () => {
      const token = localStorage.getItem('token');
      if (!token) {
        router.push('/login'); // Redirect the user to the login page if not authenticated
      }
    };
  
    checkAuthentication();
  }, [router]);
  
  
  // Function to transfer funds via REST API
  const transferFundsREST = async () => {
    try {
      const token = localStorage.getItem('token');
      const decoded = jwt_decode(token);
      const response = await axios.post('https://bankapp-hd3c.onrender.com/api/v1/transfer/', {
        sender: decoded.username,
        receiver,
        amount: parseFloat(amount),
      });
      console.log('Transfer successful (REST):', response.data);
      return response.data;
    } catch (error) {
      console.error('Error transferring funds (REST):', error);
      throw error;
    }
  };

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send request to REST API
      const restResponse = await transferFundsREST();

      // Send request to GraphQL API using Apollo Client
      const { data } = await transferFunds({
        variables: {
          sender: sender,
          receiver: receiver,
          amount: parseFloat(amount),
        },
      });
      console.log('Transfer successful (GraphQL):', data);

      // Reset form fields after successful transfer
      setSender('');
      setReceiver('');
      setAmount('');
    } catch (error) {
      console.error('Error transferring funds:', error);
      setError(error.message);
    }
  };

  return (
    <div className="flex items-center justify-center">
      <form onSubmit={handleSubmit} className="flex flex-col items-center">
        {/* Your form inputs */}
      </form>
      <RiExchangeDollarLine className="ml-4" size={40} />
    </div>
  );
};

export default TransferForm;
