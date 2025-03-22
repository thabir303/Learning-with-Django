// frontend/src/PublisherList.jsx
import React, { useEffect, useState } from 'react';
import api from './api'; // This will handle axios requests with JWT token

const PublisherList = () => {
  const [publishers, setPublishers] = useState([]);

  useEffect(() => {
    const fetchPublishers = async () => {
      try {
        const response = await api.get('http://localhost:8000/api/publishers/');
        setPublishers(response.data);
      } catch (error) {
        console.error('Error fetching publishers:', error);
      }
    };

    fetchPublishers();
  }, []);

  return (
    <div>
      <h2>Publisher List</h2>
      <ul>
        {publishers.map((publisher) => (
          <li key={publisher.id}>{publisher.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default PublisherList;
