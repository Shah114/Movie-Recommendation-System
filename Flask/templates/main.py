# Import Modules
from flask import Flask, request, jsonify, render_template
import random
import pandas as pd

# Creating Flask app
app = Flask(__name__)

# Load the dataset
df_movies = pd.read_csv('C:/Projects/RecommendationSystem/clustered_movies.csv')

# Function to recommend movies
def recommend_movie(movie_name: str, n_recommendations=5):
    movie_name = movie_name.lower()
    df_movies['name'] = df_movies['name'].str.lower()

    movie = df_movies[df_movies['name'].str.contains(movie_name, na=False)]

    if not movie.empty:
        cluster = movie['dbscan_clusters'].values[0]
        cluster_movies = df_movies[df_movies['dbscan_clusters'] == cluster]

        if len(cluster_movies) >= n_recommendations:
            recommended_movies = random.sample(list(cluster_movies['name']), n_recommendations)
        else:
            recommended_movies = list(cluster_movies['name'])

        return recommended_movies
    else:
        return ["Movie not found in the database."]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()  # Retrieve JSON data from the POST request
    movie_name = data.get('movie_name', '')  # Safely get the 'movie_name' from JSON data
    recommendations = recommend_movie(movie_name)
    return jsonify({'recommendations': recommendations})

# Main Part
if __name__ == '__main__':
    app.run(debug=True)