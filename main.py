from flask import Flask, jsonify, request
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

all_movies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

liked_movies = []
not_liked_movies = []
did_not_watch = []

def assing_val():
    m_data = {
        'original_title': all_movies.iloc[0,0],
        'poster_link': all_movies.iloc[0,1],
        'release_date': all_movies.iloc[0,2] or 'n/a',
        'duration': all_movies.iloc[0,3],
        'rating' : all_movies.iloc[0,4] /2
    }
    return m_data
@app.route('/movies')
def get_movie():
    movie_data = assing_val()
    return jsonify({
        'data': movie_data,
        'status': 'success'
    })
@app.route('/like')
def liked_movie():
    global all_movies
    movie_data = assing_val()
    liked_movie.append(movie_data)
    all_movies.drop([0],inplace = True)
    all_movies  = all_movies.reset_index(drop = True)
    return jsonify({
        'status': 'success'
    })
@app.route('/dislike')
def un_liked_movie():
    global all_movies
    movie_data = assing_val()
    not_liked_movies.append(movie_data)
    all_movies.drop([0],inplace = True)
    all_movies = all_movies.reset_index(drop = True)
    return jsonify({
        'status': 'success'
    })
@app.route('/did_not_watch')
def did_not_watch_view():
    global all_movies
    movie_data = assing_val()
    did_not_watch.append(movie_data)
    all_movies.drop([0],inplace = True)
    all_movies = all_movies.reset_index(drop = True)
    return jsonify({
        'status': 'success'
    })
if __name__ == '__main__':
    app.run()




