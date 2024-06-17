import { useRouter } from 'next/router';
import { useEffect } from 'react';

const useAuthCheck = () => {
  const router = useRouter();

  useEffect(() => {
    // Check if the user is authenticated
    const token = localStorage.getItem('token');
    if (!token) {
      // If the token is not present, redirect the user to the login page
      router.push('/login');
    }
  }, [router]);

  return null; // This hook doesn't render anything, so return null
};

export default useAuthCheck;
