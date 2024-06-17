import { gql } from '@apollo/client';

export const CREATEWITHDRAW = gql`
mutation CreateWithdraw($userId: Int!, $accountNumber: String!, $amount: Float!, $type: String!) {
  createWithdraw(userId: $userId, accountNumber: $accountNumber, amount: $amount, type: $type) {
    id
    user {
      username
    }
    accountNumber
    amount
    type
    timestamp
  }
}
`;


export const CREATETRANSACTION = gql`
mutation CreateTransaction($senderId: Int!, $receiverId: Int!, $amount: Float!, $type: String!) {
  createTransaction(senderId: $senderId, receiverId: $receiverId, amount: $amount, type: $type) {
    id
    sender {
      username
    }
    receiver {
      username
    }
    amount
    type
    timestamp
  }
}
`;
export const CREATETRANSFER = gql`
mutation CreateTransfer($senderId: Int!, $receiverId: Int!, $amount: Float!, $type: String!) {
  createTransfer(senderId: $senderId, receiverId: $receiverId, amount: $amount, type: $type) {
    transfers {
      id
      amount
      sender {
        username
        phoneNumber
        password
      }
      receiver {
        username
      }
    }
  }
}
`;

export const REGISTERUSER = gql`
mutation RegisterUser($input: RegisterUserInput!) {
  registerUser(input: $input) {
    user {
      id
      firstName
      lastName
      username
      email
      phone_number
      password
      password2
      gender
      residential_address
    }
  }
}
`;

export const CREATE_ACCESS_TOKEN = gql`
mutation CreateAccessToken($userId: Int!, $token: String!) {
  createAccessToken(userId: $userId, token: $token) {
    id
    user {
      id
      username
    }
    token
    created_at
  }
}
`;

export const CREATE_REFRESH_TOKEN = gql`
mutation CreateRefreshToken($userId: Int!, $token: String!) {
  createRefreshToken(userId: $userId, token: $token) {
    id
    user {
      id
      username
    }
    token
  }
}
`;

export const CREATEDEPOSIT = gql`
mutation CreateDeposit($userId: Int!, $amount: Float!, $accountNumber: String!, $type: String!) {
  createDeposit(userId: $userId, amount: $amount, accountNumber: $accountNumber, type: $type) {
    id
    amount
    accountNumber
    type
    timestamp
  }
}
`;

export const CREATEACCOUNT = gql`
mutation CreateAccount($userId: Int!, $balance: Float!) {
  createAccount(userId: $userId, balance: $balance) {
    id
    user {
      id
      username
    }
    balance
  }
}

`;

export const VERIFYOTP = gql`
  mutation CreateOTP($otpcode: Int!) {
    createOTP(otpcode: $otpcode) {
      otpCode
    }
  }
`;
