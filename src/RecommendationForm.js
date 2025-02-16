// src/RecommendationForm.js
import React, { useState } from "react";
import axios from "axios";
import "./App.css"; 

const RecommendationForm = () => {
  const [movieName, setMovieName] = useState("");
  const [category, setCategory] = useState("both"); // Default is both
  const [recommendations, setRecommendations] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset any previous errors

    try {
      const response = await axios.post("http://127.0.0.1:5000/recommend", {
        movie_name: movieName,
        category: category,
      });

      setRecommendations(response.data);
    } catch (err) {
      setError("Error fetching recommendations");
    }
  };

  return (
    <div className="form-container">
      <h2>Get Recommendations Based on Your Movie</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Movie Name:</label>
          <input
            type="text"
            value={movieName}
            onChange={(e) => setMovieName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Category:</label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          >
            <option value="books">Books</option>
            <option value="music">Music</option>
            <option value="both">Both</option>
          </select>
        </div>
        <button type="submit">Get Recommendations</button>
      </form>

      {error && <p>{error}</p>}

      {recommendations && (
        <div className="recommendations">
          <h3>Recommendations</h3>
          <h4>Books</h4>
          <ul>
            {recommendations.books?.map((book, index) => (
              <li key={index}>
                {book.book_name} by {book.author}
              </li>
            ))}
          </ul>

          <h4>Music</h4>
          <ul>
            {recommendations.music?.map((music, index) => (
              <li key={index}>
                {music.track_name} by {music.artist}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default RecommendationForm;
