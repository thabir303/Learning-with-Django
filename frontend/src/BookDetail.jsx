// frontend/src/BookDetail.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from './api'; // This will handle axios requests with JWT token

const BookDetail = () => {
  const [book, setBook] = useState(null);
  const { id } = useParams(); // Use the route parameter for the book ID

  useEffect(() => {
    const fetchBookDetail = async () => {
      try {
        const response = await api.get(`http://localhost:8000/api/books/${id}/`);
        setBook(response.data);
      } catch (error) {
        console.error('Error fetching book details:', error);
      }
    };

    fetchBookDetail();
  }, [id]);

  if (!book) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{book.title}</h2>
      <p>Author: {book.author.full_name}</p>
      <p>Publisher: {book.publisher.name}</p>
      <p>Published Date: {book.published_date}</p>
      <h3>Reviews:</h3>
      <ul>
        {book.reviews.map((review) => (
          <li key={review.id}>
            <p>Review: {review.review_text}</p>
            <p>Rating: {review.rating}</p>
          </li>
        ))}
      </ul>
      <h3>Genres:</h3>
      <ul>
        {book.genres.map((genre) => (
          <li key={genre.id}>{genre.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookDetail;
