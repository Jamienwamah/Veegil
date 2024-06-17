# OTP Model

**Description:**  
The OTP model represents one-time passwords generated for user authentication.

### Fields
- `id`: The unique identifier for the OTP.
- `user`: The user associated with the OTP.
- `otp_code`: The one-time password code.
- `otp_created_at`: The timestamp when the OTP was created.
- `otp_expires_at`: The timestamp when the OTP expires.
- `encrypted_otp`: The encrypted version of the OTP.
- `expiration_time`: The timestamp when the OTP expires.

## Queries

### Get All OTPs
- **Query:** `otps`
- **Description:** Returns a list of all OTPs.
- **Return Type:** List of OTP objects.

## Mutations

### Create OTP
- **Mutation:** `createOTP(userId: Int!)`
- **Description:** Creates a new OTP for the specified user.
- **Arguments:**
  - `userId`: ID of the user for whom the OTP is created.
- **Return Type:** OTP object.

### Verify OTP
- **Mutation:** `verifyOTP(otpCode: String!, otpId: Int!)`
- **Description:** Verifies the provided OTP code for the specified OTP ID.
- **Arguments:**
  - `otpCode`: The OTP code to verify.
  - `otpId`: ID of the OTP to verify.
- **Return Type:** Boolean indicating whether the OTP is valid.
