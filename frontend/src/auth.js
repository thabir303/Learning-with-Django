import axios from 'axios';

const API_URL = 'http://localhost:8000/api/token/';  

export const login = async (email, password) => {
  try {
    const response = await axios.post(API_URL, { email, password });
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    return response.data;
  } catch (error) {
    console.error('Login error: ', error);
    throw error;
  }
};

export const refreshToken = async () => {
  const refreshToken = localStorage.getItem('refresh_token');
  if (!refreshToken) return null;

  try {
    const response = await axios.post('http://localhost:8000/api/token/refresh/', { refresh: refreshToken });
    localStorage.setItem('access_token', response.data.access);
    return response.data.access;
  } catch (error) {
    console.error('Token refresh error: ', error);
    return null;
  }
};

export const getAccessToken = () => {
  // console.log(`access: ${getItem('access_token')}`);
  return localStorage.getItem('access_token');
};

export const getRefreshToken = () => {
  return localStorage.getItem('refresh_token');
};

export const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
};
