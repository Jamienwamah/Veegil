import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/router";

const useValidation = () => {
  const [errors, setErrors] = useState({});

  const validateField = (fieldName, value) => {
    switch (fieldName) {
      case "email":
        if (!value.trim()) {
          return "Please enter your email";
        }
        break;
      case "password":
        if (!value.trim()) {
          return "Please enter your password";
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

const LoginForm = ({ handleLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loginError, setLoginError] = useState("");
  const [loginSuccess, setLoginSuccess] = useState(false);
  const router = useRouter();

  const { errors, validateForm } = useValidation();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const isValid = validateForm({ email, password });
    if (isValid) {
      try {
        await handleLogin(email, password);
        setLoginSuccess(true);
        router.push("/dashboard");
      } catch (error) {
        setLoginError("Invalid email or password");
      }
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
      >
        <div className="mb-4">
          <label
            className="block text-gray-700 text-sm font-bold mb-2"
            htmlFor="email"
          >
            Email
          </label>
          <input
            className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${
              errors.email ? "border-red-500" : ""
            }`}
            id="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          {errors.email && <p className="text-red-500 text-xs italic">{errors.email}</p>}
        </div>
        <div className="mb-6">
          <label
            className="block text-gray-700 text-sm font-bold mb-2"
            htmlFor="password"
          >
            Password
          </label>
          <input
            className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline ${
              errors.password ? "border-red-500" : ""
            }`}
            id="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {errors.password && <p className="text-red-500 text-xs italic">{errors.password}</p>}
        </div>
        <div className="flex items-center justify-between">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            LogIn
          </button>
          <p className="text-sm mt-4">
            Don&apos;t have an account?{" "}
            <Link href="/register">
              <span className="text-blue-500 cursor-pointer underline">Register here</span>
            </Link>
          </p>
        </div>
      </form>
      {loginSuccess && <p className="text-green-500">Login successful. Redirecting...</p>}
      {loginError && <p className="text-red-500">{loginError}</p>}
    </div>
  );
};

export default LoginForm;
