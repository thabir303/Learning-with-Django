// frontend/src/BookReviewList.jsx
import React, { useEffect, useState } from 'react';
import api from './api'; // This will handle axios requests with JWT token

const BookReviewList = () => {
  const [bookReviews, setBookReviews] = useState([]);

  useEffect(() => {
    const fetchBookReviews = async () => {
      try {
        const response = await api.get('http://localhost:8000/api/bookreviews/');
        setBookReviews(response.data);
      } catch (error) {
        console.error('Error fetching book reviews:', error);
      }
    };

    fetchBookReviews();
  }, []);

  return (
    <div>
      <h2>Book Review List</h2>
      <ul>
        {bookReviews.map((review) => (
          <li key={review.id}>
            <p>Review: {review.review_text}</p>
            <p>Rating: {review.rating}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookReviewList;
