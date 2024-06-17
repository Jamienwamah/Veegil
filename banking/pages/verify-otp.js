import React, { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/router";
import { useMutation } from "@apollo/client";
import axios from "axios";
import VerifyOTPForm from "../components/VerifyOTPForm";
import { VERIFYOTP } from "../components/graphql/mutations";
import clients from "../components/apollo/client";

const VerifyOTPPage = () => {
  const router = useRouter();
  const [resendStatus, setResendStatus] = useState(null);
  const [error, setError] = useState(null);

  const [verifyOTP] = useMutation(VERIFYOTP, {
    client: clients.otp,
    onError: (error) => {
      console.error("Error verifying your otp (GraphQL):", error.message);
      setError(error.message);
    },
    onCompleted: () => {
      console.log(
        "OTP verified successfully, please proceed to sign in (GraphQL)"
      );
      router.push("/login", { message: "Please login" });
    },
  });

  const handleSubmit = useCallback(
    async (otp) => {
      if (clients.auth) {
        try {
          await verifyOTP({
            variables: {
              otpcode: otp,
            },
          });
        } catch (error) {
          console.error("OTP verification error (GraphQL):", error);
          setError(error.message);
        }
      } else {
        const userId = router.query.userId;
        if (!userId) {
          console.error("User ID not found in query parameters");
          setError("User ID not found");
          return;
        }
        try {
          const response = await axios.post(
            `https://bankapp-hd3c.onrender.com/api/v1/auth/verify-otp/${userId}`,
            { otp }
          );
          console.log("OTP verification successful (REST):", response.data);
          router.push("/login");
        } catch (error) {
          console.error("OTP verification error (REST):", error.message);
          setError(error.message);
        }
      }
    },
    [clients.auth, router.query.userId, verifyOTP]
  );

  useEffect(() => {
    if (router.query.otp) {
      handleSubmit(router.query.otp);
    }
  }, [router.query.otp, handleSubmit]);

  const handleResendOTP = useCallback(async () => {
    try {
      const userId = router.query.userId;
      if (!userId) {
        console.error("User ID not found in query parameters");
        setError("User ID not found");
        return;
      }
      // Call your REST API endpoint to resend OTP
      const response = await axios.post(
        `https://bankapp-hd3c.onrender.com/api/v1/auth/resend-otp/${userId}`
      );
      setResendStatus(response.data.message);
    } catch (error) {
      console.error("Error resending OTP:", error.message);
      setError(error.message);
    }
  }, [router.query.userId]);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4 text-center">Verify OTP</h1>
      <VerifyOTPForm handleSubmit={handleSubmit} />
      <div className="flex items-center justify-center mt-4">
        <p className="text-blue-500 hover:underline">
          Didn&apos;t receive OTP?
        </p>
        <button
          className="text-blue-500 hover:underline ml-2"
          onClick={handleResendOTP}
        >
          Resend
        </button>
      </div>
      {resendStatus && <p className="mt-4">{resendStatus}</p>}
    </div>
  );
};

export default VerifyOTPPage;
