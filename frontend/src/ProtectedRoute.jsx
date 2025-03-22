// frontend/src/ProtectedRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';
import { getAccessToken } from './auth';

const ProtectedRoute = ({ element, ...rest }) => {
  const isAuthenticated = getAccessToken();
  console.log(isAuthenticated);
  return isAuthenticated ? element : <Navigate to="/login" />;
};

export default ProtectedRoute;
