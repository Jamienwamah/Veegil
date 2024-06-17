import React, { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';
import LoginForm from '../components/LoginForm';
import { useMutation } from '@apollo/client';
import { CREATE_ACCESS_TOKEN  } from '../components/graphql/mutations';
import clients from '../components/apollo/client'; 

const Login = () => {
  const router = useRouter();
  const [error, setError] = useState(null);

  // Apollo Client mutation hook for logging in user
  const [loginUser] = useMutation(CREATE_ACCESS_TOKEN, {
    client: clients.login,
    onError: (error) => {
      console.error('Error logging in (GraphQL):', error.message);
      setError(error.message);
    },
    onCompleted: (data) => {
      console.log('Login successful (GraphQL)', data);
      // Redirect to dashboard on successful login
      router.push('/dashboard');
    },
  });

  const handleLogin = async (email, password) => {
    try {
      // Make request to REST API
      const restApiResponse = await axios.post('https://bankapp-hd3c.onrender.com/api/v1/auth/jwt/create/', { email, password });
      console.log('Login successful (REST)', restApiResponse.data);
      // Redirect to dashboard on successful login
      router.push('/dashboard');

      // Make request to GraphQL API
      const graphQlApiResponse = await loginUser({
        variables: { username, password },
      });
      console.log('Login successful (GraphQL)', graphQlApiResponse.data);
    } catch (error) {
      console.error('Login error', error);
      setError(error.message);
    }
  };

  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold text-black mb-4">Login</h2>
      <LoginForm handleLogin={handleLogin} />
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default Login;
