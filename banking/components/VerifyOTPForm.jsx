import { useState } from 'react';

const VerifyOTPForm = ({ handleSubmit }) => {
  const [otp, setOTP] = useState('');

  const handleVerify = (e) => {
    e.preventDefault();
    handleSubmit(otp);
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <h1 className="text-2xl font-bold mb-4">Verify OTP</h1>
        <form onSubmit={handleVerify}>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-4 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            placeholder="Enter OTP"
            value={otp}
            onChange={(e) => setOTP(e.target.value)}
          />
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Verify
          </button>
        </form>
      </div>
    </div>
  );
};

export default VerifyOTPForm;
