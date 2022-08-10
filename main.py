from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, not_liked_articles, did_not_read
#from demographic_filtering import output
#from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    movie_data = {
        "title": all_articles[0][19],
        "rating": all_articles[0][20],
        "overview": all_articles[0][9]
    }
 

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    movie = all_articles[0]
    liked_articles.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_articles():
    movie = all_articles[0]
    not_liked_articles.append(not_liked_articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-read", methods=["POST"])
def did_not_read_view():
    movie = all_articles[0]
    did_not_read.append(movie)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    movie_data = []
    for all_articles in output:
        _d = {
            "title": articles[0],
            "rating": articles[4],
            "overview": articles[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_movies():
    all_recommended = []
    for liked_articles in liked_articles:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        movie_data.append(_d)

if __name__ == "__main__":
  app.run()