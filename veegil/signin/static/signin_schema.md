# Access Token Model

**Description:**  
The `AccessToken` model represents access tokens associated with users.

### Fields
- `id`: The unique identifier for the access token.
- `user`: The user associated with the access token.
- `token`: The access token string.
- `created_at`: The timestamp when the access token was created.

---

# Refresh Token Model

**Description:**  
The `RefreshToken` model represents refresh tokens associated with users.

### Fields
- `id`: The unique identifier for the refresh token.
- `user`: The user associated with the refresh token.
- `token`: The refresh token string.

---

## GraphQL Schema

```graphql
type AccessToken {
  id: ID!
  user: User!
  token: String!
  createdAt: DateTime!
}

type RefreshToken {
  id: ID!
  user: User!
  token: String!
}

type Query {
  # Define any queries here
}

type Mutation {
  # Define any mutations here
}
