from flask import Flask, render_template, request
from recommender import get_recommendations, get_movie_titles

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", movies=get_movie_titles())

@app.route("/recommend", methods=["POST"])
def recommend():
    movie = request.form.get("movie", "").strip()
    recommendations = get_recommendations(movie)
    return render_template(
        "index.html",
        movies=get_movie_titles(),
        selected_movie=movie,
        recommendations=recommendations,
        searched=True
    )

if __name__ == "__main__":
    app.run(debug=True)
