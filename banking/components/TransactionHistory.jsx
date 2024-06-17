import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaMoneyCheckAlt } from 'react-icons/fa';
import { useMutation } from '@apollo/client';
import { useRouter } from 'next/router';
import { CREATETRANSACTION } from '../components/graphql/mutations';
import clients from '../components/apollo/client';

const TransactionHistory = () => {
  // State Management
  const [transactions, setTransactions] = useState([]);
  const [error, setError] = useState(null);
  const [user, setUser] = useState('');
  const [sender, setSender] = useState('');
  const [receiver, setReceiver] = useState('');
  const [amount, setAmount] = useState('');

  // Router
  const router = useRouter();

  // Apollo Client
  const [createTransaction] = useMutation(CREATETRANSACTION, {
    client: clients.transactionhistory,
    onError: (error) => {
      console.error('Error displaying transaction history of this account (GraphQL):', error.message);
      setError(error.message);
    },
    onCompleted: () => {
      console.log('Your transaction history (GraphQL)');
      // Reset form fields after retrieving transaction history
      setUser('');
      setSender('');
      setReceiver('');
      setAmount('');
      error('');
    },
  });

  useEffect(() => {
    // Fetch transaction history
    const fetchTransactions = async () => {
      try {
        const response = await axios.get('https://bankapp-hd3c.onrender.com/api/v1/transaction-history');
        setTransactions(response.data);
      } catch (error) {
        console.error('Error fetching transaction history:', error);
        setError('Error fetching transaction history');
      }
    };

    // Call Apollo mutation for deposit
    const result = createTransaction({
      variables: {
        user,
        sender,
        receiver,
        amount
      }
    });

    fetchTransactions(); // Now let's fetchTransactions function when the component mounts
  }, []); // This is an empty dependency array ensures the effect runs only once, when the component mounts

  return (
    <div className='w-full col-span-1 relative lg:h-[70vh] h-[50vh] m-auto p-4 border rounded-lg bg-white overflow-scroll'>
      <h1>Transaction History</h1>
      <ul>
        {transactions.map((transaction, id) => (
          <li
            key={id}
            className='bg-gray-50 hover:bg-gray-100 rounded-lg my-3 p-2 flex items-center cursor-pointer'
          >
            <div className='bg-blue-100 rounded-lg p-3'>
              <FaMoneyCheckAlt className='text-blue-800' />
            </div>
            <div className='pl-4'>
              <p className='text-gray-800 font-bold'>${transaction.amount}</p>
              <p className='text-gray-400 text-sm'>{transaction.customerName}</p>
            </div>
            <p className='lg:flex md:hidden absolute right-6 text-sm'>{transaction.date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionHistory;
