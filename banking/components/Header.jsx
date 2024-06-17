import React from 'react';

const Header = ({ user }) => {
  return (
    <div className='flex justify-between px-4 pt-4'>
      <h2>Dashboard</h2>
      <h2>Welcome Back, {user}</h2> 
    </div>
  );
};

export default Header;
