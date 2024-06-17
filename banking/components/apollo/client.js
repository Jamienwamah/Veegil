import { ApolloClient, InMemoryCache } from '@apollo/client';

// Define the base URI for your GraphQL APIs
const baseUri = 'https://bankapp-hd3c.onrender.com/api/v1/';

// Define the endpoints for each GraphQL API
const graphqlEndpoints = {
  transfer: `${baseUri}transfergraphql/`,
  balance: `${baseUri}balancegraphql/`,
  deposit: `${baseUri}depositgraphql/`,
  wihdraw: `${baseUri}withdrawgraphql/`,
  transactionhistory: `${baseUri}transactionhistorygraphql/`,
  login: `${baseUri}logingraphql/`,
  register: `${baseUri}registergraphql/`,
  otp: `${baseUri}otpgraphql/`,
};

// Create a function to generate Apollo Client instances for each GraphQL API
const createApolloClient = (endpoint) => {
  return new ApolloClient({
    uri: endpoint,
    cache: new InMemoryCache(),
  });
};

// Create an object to hold Apollo Client instances for each GraphQL API
const clients = {};
for (const key in graphqlEndpoints) {
  clients[key] = createApolloClient(graphqlEndpoints[key]);
}

// Export the object containing Apollo Client instances
export default clients;
