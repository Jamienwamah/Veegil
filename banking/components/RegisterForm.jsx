import React, { useState } from "react";

// Validate fields before submitting
const useValidation = () => {
  const [errors, setErrors] = useState({});

  const validateField = (fieldName, value) => {
    switch (fieldName) {
      case "firstname":
        if (!value.trim()) {
          return "Please enter your first name";
        }
        break;
      case "lastname":
        if (!value.trim()) {
          return "Please enter your last name";
        }
        break;
      case "username":
        if (!value.trim()) {
          return "Please enter a username";
        }
        break;
      case "email":
        if (!value.trim()) {
          return "Please enter your email";
        }
        break;
      case "phone_number":
        if (!value.trim()) {
          return "Please enter your phone number";
        }
        break;
      case "password":
        if (!value.trim()) {
          return "Please enter a password";
        }
        break;
      case "confirmPassword":
        if (!value.trim()) {
          return "Please confirm your password";
        } else if (value.trim() !== formData.password.trim()) {
          return "Passwords do not match";
        }
        break;
      case "gender":
        if (!value.trim()) {
          return "Please select your gender";
        }
        break;
      case "residentialAddress":
        if (!value.trim()) {
          return "Please enter your residential address";
        }
        break;
      default:
        break;
    }
    return "";
  };

  const validateForm = (formData) => {
    const validationErrors = {};
    for (const key in formData) {
      if (formData.hasOwnProperty(key)) {
        const error = validateField(key, formData[key]);
        if (error) {
          validationErrors[key] = error;
        }
      }
    }
    setErrors(validationErrors);
    return Object.keys(validationErrors).length === 0;
  };

  return { errors, validateForm };
};

const RegisterForm = ({ handleRegister }) => {
  const { errors, validateForm } = useValidation();
  const [formData, setFormData] = useState({
    firstname: "",
    lastname: "",
    username: "",
    email: "",
    phone_number: "",
    password: "",
    confirmPassword: "",
    gender: "",
    residentialAddress: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    setErrors((prevErrors) => ({
      ...prevErrors,
      [name]: "", // Clear the error when user starts typing
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const isValid = validateForm(formData);
    if (isValid) {
      handleRegister(formData);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8 z-20">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
        <input
          type="text"
          name="firstname"
          placeholder="First Name"
          value={formData.firstname}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.firstname ? "border-red-500" : ""
          }`}
        />
        {errors.firstname && (
          <p className="text-red-500 text-xs italic">{errors.firstname}</p>
        )}
        <input
          type="text"
          name="lastname"
          placeholder="Last Name"
          value={formData.lastname}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.lastname ? "border-red-500" : ""
          }`}
        />
        {errors.lastname && (
          <p className="text-red-500 text-xs italic">{errors.lastname}</p>
        )}
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.username ? "border-red-500" : ""
          }`}
        />
        {errors.username && (
          <p className="text-red-500 text-xs italic">{errors.username}</p>
        )}
        <input
          type="text"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.email ? "border-red-500" : ""
          }`}
        />
        {errors.email && (
          <p className="text-red-500 text-xs italic">{errors.email}</p>
        )}
        <input
          type="text"
          name="phone_number"
          placeholder="Phone Number"
          value={formData.phone_number}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.phone_number ? "border-red-500" : ""
          }`}
        />
        {errors.phone_number && (
          <p className="text-red-500 text-xs italic">{errors.phone_number}</p>
        )}

        <input
          type="text"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.password ? "border-red-500" : ""
          }`}
        />
        {errors.password && (
          <p className="text-red-500 text-xs italic">{errors.password}</p>
        )}
        <input
          type="text"
          name="password"
          placeholder="Confirm Password"
          value={formData.password}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.password ? "border-red-500" : ""
          }`}
        />
        {errors.password && (
          <p className="text-red-500 text-xs italic">{errors.password}</p>
        )}
        <select
          id="gender"
          value={formData.gender}
          onChange={(e) => {
            setFormData({ ...formData, gender: e.target.value });
            setErrors((prevErrors) => ({
              ...prevErrors,
              gender: "",
            }));
          }}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.gender ? "border-red-500" : ""
          }`}
        >
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <input
          type="text"
          name="residentialAddress"
          placeholder="Residential Address"
          value={formData.residentialAddress}
          onChange={handleChange}
          className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mb-4 ${
            errors.residentialAddress ? "border-red-500" : ""
          }`}
        />
        {errors.residentialAddress && (
          <p className="text-red-500 text-xs italic">
            {errors.residentialAddress}
          </p>
        )}
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterForm;
