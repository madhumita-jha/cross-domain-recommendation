import pandas as pd

# Load clean datasets
movie_df = pd.read_csv("dataset/cleaned_movie_data.csv")
book_df = pd.read_csv("dataset/clean_books.csv")
music_df = pd.read_csv("dataset/cleaned_music_data.csv")

# Rename columns for consistency
movie_df.rename(columns={"genre": "Genres"}, inplace=True)
book_df.rename(columns={"genre": "Genres"}, inplace=True)
music_df.rename(columns={"track_genre": "Genres"}, inplace=True)

# Convert genre strings to lowercase for consistency
movie_df["Genres"] = movie_df["Genres"].str.lower()
book_df["Genres"] = book_df["Genres"].str.lower()
music_df["Genres"] = music_df["Genres"].str.lower()

# Create mapping dictionaries
movie_to_books = []
movie_to_music = []

# Mapping movies to books based on genre
for genre in movie_df["Genres"].unique():
    related_books = book_df[book_df["Genres"].str.contains(genre, na=False, case=False)]
    for _, row in related_books.iterrows():
        movie_to_books.append({
            "movie_genre": genre,
            "book_name": row["name"],
            "author": row["author"]
        })

# Mapping movies to music based on genre
for genre in movie_df["Genres"].unique():
    related_music = music_df[music_df["Genres"].str.contains(genre, na=False, case=False)]
    for _, row in related_music.iterrows():
        movie_to_music.append({
            "movie_genre": genre,
            "artist": row["artists"],
            "album_name": row["album_name"],
            "track_name": row["track_name"]
        })

# Save mappings as CSV files for later use
movie_books_df = pd.DataFrame(movie_to_books)
movie_books_df.to_csv("movie_to_books.csv", index=False)

movie_music_df = pd.DataFrame(movie_to_music)
movie_music_df.to_csv("movie_to_music.csv", index=False)

print("Mappings saved successfully!")
