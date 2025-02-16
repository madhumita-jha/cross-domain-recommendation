from flask import Flask, request, jsonify
from flask_cors import CORS;
from recommendation_system import recommend_based_on_genre  # Import the updated function

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_name = data.get("movie_name")
    category = data.get("category")  # Either "books", "music", or "both"

    if not movie_name or not category:
        return jsonify({"error": "Missing movie_name or category"}), 400

    recommendations = recommend_based_on_genre(movie_name, category)

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
