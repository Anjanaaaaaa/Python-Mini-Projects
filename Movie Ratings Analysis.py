# Movie Ratings Analysis - Mini Project 1

import pandas as pd

# Load the dataset (replace 'movies.csv' with your actual file name)
df = pd.read_csv("movies.csv")

# Display first few rows to understand structure
print("Sample Data:")
print(df.head())

# Find top 10 highest-rated movies
top_movies = df.sort_values(by="rating", ascending=False).head(10)
print("\nTop 10 Highest-Rated Movies:")
print(top_movies[["title", "rating"]])
