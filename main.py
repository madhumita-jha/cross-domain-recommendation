import os
import pandas as pd

# Get the current directory of this file
base_dir = os.path.dirname(__file__)

# Load cleaned datasets
movies_df = pd.read_csv(os.path.join(base_dir, "dataset", "cleaned_movie_data.csv"))
music_df = pd.read_csv(os.path.join(base_dir, "dataset", "cleaned_music_data.csv"))
books_df = pd.read_csv(os.path.join(base_dir, "dataset", "clean_books.csv"))

# Inspect the datasets
print("Movies Dataset:")
print(movies_df.head())

print("\nMusic Dataset:")
print(music_df.head())

print("\nBooks Dataset:")
print(books_df.head())
