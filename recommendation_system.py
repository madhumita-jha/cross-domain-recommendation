import pandas as pd
import random

# Load pre-saved movie-to-book and movie-to-music datasets
movie_books_df = pd.read_csv("dataset/movie_to_books.csv")
movie_music_df = pd.read_csv("dataset/movie_to_music.csv")
movies_df = pd.read_csv("dataset/movie_data.csv")

def recommend_based_on_genre(movie_name, recommendation_type="both"):

    # Find the genre of the given movie
    movie_row = movies_df[movies_df["title"].str.lower() == movie_name.lower()]

    if not movie_row.empty:
        user_genre = movie_row.iloc[0]["genre"]  # Get the movie's genre
        filtered_books = movie_books_df[movie_books_df["movie_genre"] == user_genre]
        filtered_music = movie_music_df[movie_music_df["movie_genre"] == user_genre]
    else:
        user_genre = None  # Movie not found, fallback to random recommendations
        filtered_books = pd.DataFrame()  
        filtered_music = pd.DataFrame()

    # Initialize recommendation lists
    recommended_books = []
    recommended_music = []

    # If books exist for the genre, pick random 3; otherwise, return random books
    if not filtered_books.empty:
        recommended_books = filtered_books[["book_name", "author"]].sample(min(3, len(filtered_books))).to_dict(orient="records")
    else:
        recommended_books = movie_books_df.sample(3)[["book_name", "author"]].to_dict(orient="records")
    
    # If music exists for the genre, pick random 3; otherwise, return random music
    if not filtered_music.empty:
        recommended_music = filtered_music[["track_name", "artist"]].sample(min(3, len(filtered_music))).to_dict(orient="records")
    else:
        recommended_music = movie_music_df.sample(3)[["track_name", "artist"]].to_dict(orient="records")

    # Response message if movie is not found
    response_message = f"Movie '{movie_name}' not found. Showing general recommendations." if user_genre is None else None

    # Return recommendations based on the user's choice
    recommendations = {"books": recommended_books, "music": recommended_music}
    if recommendation_type == "books":
        recommendations = {"books": recommended_books}
    elif recommendation_type == "music":
        recommendations = {"music": recommended_music}

    # Include a message only if the movie wasn't found
    if response_message:
        recommendations["message"] = response_message

    return recommendations
