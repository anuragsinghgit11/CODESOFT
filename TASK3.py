#TASK 3
#RECOMMENDATION SYSTEM
#Create a simple recommendation system that suggests items to
#users based on their preferences. You can use techniques like
#collaborative filtering or content-based filtering to recommend
#movies, books, or products to users.

import pandas as pd

# Sample dataset of user preferences
user_preferences = {
    'user_id': [1, 2, 3, 4, 5],
    'movie_title': ['The Shawshank Redemption', 'The Godfather', 'Pulp Fiction', 'The Dark Knight', 'Inception'],
    'genre': ['Drama', 'Crime', 'Crime', 'Action', 'Sci-Fi'],
    'rating': [9.3, 9.2, 8.9, 9.0, 8.8]
}

# Convert the dictionary to a DataFrame
df_preferences = pd.DataFrame(user_preferences)

# Function to recommend items based on user preferences
def recommend_items(user_id, df_preferences, num_recommendations=5):
    # Get the user's preferences
    user_preferences = df_preferences[df_preferences['user_id'] == user_id]
    
    # Calculate the similarity between the user's preferences and all other movies
    df_preferences['similarity'] = df_preferences.apply(lambda row: calculate_similarity(user_preferences, row), axis=1)
    
    # Sort the DataFrame by similarity in descending order
    df_preferences = df_preferences.sort_values(by='similarity', ascending=False)
    
    # Remove the user's preferences from the recommended items
    recommended_items = df_preferences[df_preferences['user_id'] != user_id].head(num_recommendations)
    
    return recommended_items

# Function to calculate the similarity between two movie preferences
def calculate_similarity(user_preferences, movie_preferences):
    # In this example, we'll use genre and rating as similarity factors
    genre_similarity = int(user_preferences['genre'] == movie_preferences['genre'])
    rating_similarity = abs(user_preferences['rating'] - movie_preferences['rating']) / 10
    
    # Combine the similarity factors
    similarity = genre_similarity * 0.5 + (1 - rating_similarity) * 0.5
    
    return similarity

# Example usage
user_id = 1
recommended_items = recommend_items(user_id, df_preferences)
print("Recommended items for user", user_id, ":\n", recommended_items[['movie_title', 'genre', 'rating']])
