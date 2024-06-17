import React, { useState } from "react";
import axios from "axios";
import { useRouter } from "next/router";
import RegisterForm from "../components/RegisterForm";
import { useMutation } from "@apollo/client";
import { REGISTERUSER } from "../components/graphql/mutations";
import clients from "../components/apollo/client";

const Register = () => {
  const router = useRouter();
  const [errors, setErrors] = useState({});
  const [successMessage, setSuccessMessage] = useState("");
  const [registering, setRegistering] = useState(false);
  const [userData, setUserData] = useState({
    firstname: "",
    lastname: "",
    username: "",
    email: "",
    phone_number: "",
    password: "",
    password2: "",
    gender: "",
    residential_address: "",
  });

  const [registerUser] = useMutation(REGISTERUSER, {
    client: clients.register,
    onError: (error) => {
      console.error("Error creating register (GraphQL):", error.message);
      setErrors((prevErrors) => ({
        ...prevErrors,
        graphqlError:
          "An error occurred during registration. Please try again later.",
      }));
    },
    onCompleted: () => {
      console.log("Registration successful, please verify OTP (GraphQL)");
      setSuccessMessage(
        "Account created successfully! An OTP to confirm your verification has been sent."
      );
      redirectToVerifyOTP();
    },
  });

  const handleRegister = async (userData) => {
    setRegistering(true);
    try {
      // Make request to REST API
      const restApiResponse = await axios.post(
        "https://bankapp-hd3c.onrender.com/api/v1/auth/register/",
        userData
      );
      console.log(
        "Registration successful, please verify OTP (REST)",
        restApiResponse.data
      );

      // Make request to GraphQL API
      const graphQlApiResponse = await registerUser({
        variables: userData,
      });
      console.log("Registration successful (GraphQL)", graphQlApiResponse.data);

      setSuccessMessage(
        "Account created successfully! An OTP to confirm your verification has been sent."
      );
      redirectToVerifyOTP();
    } catch (error) {
      console.error("Registration error", error);
      handleRegistrationError(error);
    } finally {
      setRegistering(false); // Reset registering state when processing is done
    }
  };

  const handleRegistrationError = (error) => {
    if (error.response && error.response.data) {
      setErrors(error.response.data);
    } else if (error.graphQLErrors && error.graphQLErrors.length > 0) {
      const graphQlError = error.graphQLErrors[0].message;
      setErrors((prevErrors) => ({
        ...prevErrors,
        graphqlError: graphQlError,
      }));
    } else {
      setErrors({
        genericError:
          "An error occurred during registration. Please try again later.",
      });
    }
  };

  const redirectToVerifyOTP = () => {
    router.push("/verify-otp", { message: "Please verify your OTP" });
  };

  const validateFields = () => {
    const requiredFields = [
      "firstname",
      "lastname",
      "username",
      "email",
      "phone_number",
      "password",
      "password2",
      "gender",
      "residential_address",
    ];
    const newErrors = {};

    requiredFields.forEach((field) => {
      if (!userData[field]) {
        newErrors[field] = `${
          field.charAt(0).toUpperCase() + field.slice(1)
        } is required.`;
      }
    });

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0; // Return true if there are no errors
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const isValid = validateFields();

    if (isValid) {
      handleRegister(userData);
    } else {
      setSuccessMessage(""); // Clear success message if there are errors
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
  };

  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold text-black mb-4">Register</h2>
      <RegisterForm
        handleSubmit={handleSubmit}
        handleInputChange={handleInputChange}
        errors={errors}
        registering={registering}
      />
      {successMessage && (
        <div className="text-green-500 mt-2">{successMessage}</div>
      )}
      {Object.keys(errors).length > 0 && (
        <div className="text-red-500 mt-2">
          {Object.keys(errors).map((key) => (
            <p key={key}>{errors[key]}</p>
          ))}
        </div>
      )}
    </div>
  );
};


export default Register;