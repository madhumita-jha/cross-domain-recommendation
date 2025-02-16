import pandas as pd

# Load the movie dataset
movie_data = pd.read_csv('dataset/movie_data.csv')

# Print the original movie data
print("Original Movies Dataset:")
print(movie_data.head())

# Clean the 'movie' column by removing the 'http://dbpedia.org/resource/' part
movie_data['movie'] = movie_data['movie'].apply(lambda x: x.replace("http://dbpedia.org/resource/", "") if isinstance(x, str) else x)

# Clean the 'genre' column by removing the 'http://dbpedia.org/resource/' part
movie_data['genre'] = movie_data['genre'].apply(lambda x: x.replace("http://dbpedia.org/resource/", "") if isinstance(x, str) else x)

# Display cleaned movie data
print("\nCleaned Movie Data:")
print(movie_data.head())

# Save the cleaned movie data to a new file
movie_data.to_csv('dataset/cleaned_movie_data.csv', index=False)

print("\nCleaned movie data saved to 'dataset/cleaned_movie_data.csv'")

# Load the dataset
df = pd.read_csv('dataset/music_data.csv')

# Select only the required columns
cleaned_data = df[['track_genre', 'artists', 'album_name', 'track_name']]

# Save the cleaned data to a new CSV file
cleaned_data.to_csv('cleaned_music_data.csv', index=False, encoding='utf-8')

print("Cleaned music data saved as 'cleaned_music_data.csv'.")
