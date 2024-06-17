# User Model

Description:
The User model represents users in the application.

### Fields
- `id`: The unique identifier for the user.
- `first_name`: The first name of the user.
- `last_name`: The last name of the user.
- `username`: The unique username of the user.
- `email`: The unique email address of the user.
- `email_verified`: Indicates whether the user's email address is verified.
- `verification_code`: The verification code associated with the user's email address.
- `date_of_birth`: The date of birth of the user.
- `password`: The password of the user.
- `gender`: The gender of the user.
- `residential_address`: The residential address of the user.
- `referral_code`: The referral code associated with the user.
- `wallet_address`: The wallet address of the user.
- `is_active`: Indicates whether the user account is active.
- `is_staff`: Indicates whether the user has staff privileges.
- `phone_number`: The phone number of the user.
- `groups`: The groups the user belongs to.
- `user_permissions`: The permissions assigned to the user.

### Methods
- `save()`: Saves the user instance. Generates a unique account number if not already set.
- `generate_account_number()`: Generates a unique account number based on UUID.
- `__str__()`: Returns the username of the user.
- `tokens()`: Generates and returns refresh and access tokens for the user.

