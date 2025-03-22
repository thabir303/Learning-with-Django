import axios from 'axios';
import { getAccessToken, getRefreshToken } from './auth';

const API_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_URL,
});

// Add the Authorization header for all requests
api.interceptors.request.use(
  (config) => {
    const token = getAccessToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Handle expired token and refresh it
api.interceptors.request.use(
  (response) => response, 
  async (error) => {
    if(error.response.status===401){
      const refreshToken = getRefreshToken();
      if(refreshToken){
        try {
          const response = await axios.post('http://localhost:8000/api/token/refresh',{
            refresh:refreshToken,
          });
          localStorage.setItem('access_token',response.data.access);
          error.config.headers['Authorization'] = `Bearer ${response.data.access}`;
          return axios(error.config);
        } catch (error) {
          console.error('Error refreshing token:', error);
        }
      }
    }
    return Promise.reject(error);
  }
);

export default api;

