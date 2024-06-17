import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { RiExchangeDollarLine, RiBankLine, RiArrowUpDownLine, RiLoginCircleLine, RiUserAddLine } from 'react-icons/ri';

const Sidebar = ({ children }) => {
  return (
    <div className='flex relative'>
      <div className='fixed w-20 h-screen p-4 bg-gray-900 border-r-[1px] flex flex-col justify-between z-10'>
        <div className='flex flex-col items-center'>
          <Link href='/'>
            <div className='bg-purple-800 text-white p-3 rounded-lg inline-block'>
              {/* setting up my logo */}
              <Image src="/Keystone-Bank-Logo.jpg" alt="Keystone Bank" width={150} height={40} />
            </div>
          </Link>
          <span className='border-b-[1px] border-gray-200 w-full p-2'></span>
          <Link href='/transfer'> {/* Link to the transfer form page */}
            <div className='bg-gray-100 hover:bg-gray-200 cursor-pointer my-4 p-3 rounded-lg inline-block'>
              <RiExchangeDollarLine size={20} /> {/* Display transfer icon */}
            </div>
          </Link>
          <Link href='/withdraw'> {/* Link to the withdraw page */}
            <div className='bg-gray-100 hover:bg-gray-200 cursor-pointer my-4 p-3 rounded-lg inline-block'>
              <RiArrowUpDownLine size={20} /> {/* Display withdraw icon */}
            </div>
          </Link>
          <Link href='/deposit'> {/* Link to the deposit page */}
            <div className='bg-gray-100 hover:bg-gray-200 cursor-pointer my-4 p-3 rounded-lg inline-block'>
              <RiBankLine size={20} /> {/* Display deposit icon */}
            </div>
          </Link>
          <Link href='/register'> {/* Link to the register page */}
            <div className='bg-gray-100 hover:bg-gray-200 cursor-pointer my-4 p-3 rounded-lg inline-block'>
              <RiUserAddLine size={20} /> {/* Display register icon */}
            </div>
          </Link>
          <Link href='/login'> {/* Link to the login page */}
            <div className='bg-gray-100 hover:bg-gray-200 cursor-pointer my-4 p-3 rounded-lg inline-block'>
              <RiLoginCircleLine size={20} /> {/* Display login icon */}
            </div>
          </Link>
        </div>
      </div>
      <main className='ml-20 w-full'>{children}</main>
    </div>
  );
};

export default Sidebar;
