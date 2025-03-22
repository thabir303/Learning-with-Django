// frontend/src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './Login';
import BookList from './BookList';
import BookDetail from './BookDetail';
import PublisherList from './PublisherList';
import AuthorList from './AuthorList';
import GenreList from './GenreList';
import BookReviewList from './BookReviewList';
import ProtectedRoute from './ProtectedRoute';
import Navbar from './Navbar';
import { useState } from 'react';
import { useEffect } from 'react';
import { getAccessToken } from './auth';
import Logout from './Logout';

function App() {
  const [isAuthenticated,setIsAuthenticated] = useState(false)

  useEffect(() => {
    const token = getAccessToken();
    if(token){
      setIsAuthenticated(true);
    }else 
      setIsAuthenticated(false);
  },[]);

  return (
    <Router>
      <div className="App">
      <Navbar />
        <Routes>
          <Route 
            path="/login" 
            element={<Login />} 
          />

          <Route
            path="/dashboard"
            element={<ProtectedRoute isAuthenticated={isAuthenticated} element={<BookList />} />}
          />

          <Route
            path="/books/:id"
            element={<ProtectedRoute isAuthenticated={isAuthenticated} element={<BookDetail />} />}
          />

          <Route
            path="/publishers"
            element={<ProtectedRoute isAuthenticated={isAuthenticated}  element={<PublisherList />} />}
          />

          <Route
            path="/authors"
            element={<ProtectedRoute isAuthenticated={isAuthenticated}  element={<AuthorList />} />}
          />

          <Route
            path="/genres"
            element={<ProtectedRoute isAuthenticated={isAuthenticated}  element={<GenreList />} />}
          />

          <Route
            path="/bookreviews"
            element={<ProtectedRoute isAuthenticated={isAuthenticated}  element={<BookReviewList />} />}
          />

          <Route
            path="/logout"
            element={<ProtectedRoute isAuthenticated={isAuthenticated}  element={<Logout />} />}
          />
          <Route 
            path="/" 
            element={<Login />} 
          />
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
