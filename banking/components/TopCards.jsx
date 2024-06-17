import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopCards = () => {
  const [balance, setBalance] = useState(0);

  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const response = await axios.get('https://bankapp-hd3c.onrender.com/api/v1/balance/');
        setBalance(response.data.balance); 
      } catch (error) {
        console.error('Error fetching balance:', error);
      }
    };

    fetchBalance(); 
  }, []);

  return (
    <div className='grid lg:grid-cols-5 gap-4 p-4'>
      <div className='lg:col-span-2 col-span-1 bg-white flex justify-between w-full border p-4 rounded-lg'>
        <div className='flex flex-col w-full pb-4'>
          <p className='text-2xl font-bold'>{balance}</p>
          <p className='text-gray-600'>Customer</p>
        </div>
        <p className='bg-green-200 flex justify-center items-center p-2 rounded-lg'>
          <span className='text-green-700 text-lg'>+18%</span>
        </p>
      </div>
      <div className='lg:col-span-2 col-span-1 bg-white flex justify-between w-full border p-4 rounded-lg'>
        <div className='flex flex-col w-full pb-4'>
          <p className='text-2xl font-bold'>$1,437,876</p>
          <p className='text-gray-600'>YTD Revenue</p>
        </div>
        <p className='bg-green-200 flex justify-center items-center p-2 rounded-lg'>
          <span className='text-green-700 text-lg'>+11%</span>
        </p>
      </div>
      <div className='bg-white flex justify-between w-full border p-4 rounded-lg'>
        <div className='flex flex-col w-full pb-4'>
          <p className='text-2xl font-bold'>{balance}</p>
          <p className='text-gray-600'>Balance</p>
        </div>
        <p className='bg-green-200 flex justify-center items-center p-2 rounded-lg'>
          <span className='text-green-700 text-lg'>+17%</span>
        </p>
      </div>
    </div>
  );
};

export default TopCards;
