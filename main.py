from flask import Flask, jsonify, request
import pandas as pd
import csv 

details = []
with open('movies.csv', encoding="utf-8") as f:
     reader = csv.reader(f)
     data = list(reader)
     details = data[1:]


liked_movies = []
not_liked_movies = []
did_not_watched_movies = []

main = Flask(__name__)

@main.route("/get-movie")

def get_movies():
     return jsonify({
          "data": details[0],
          "status": "success",
     })

@main.route("/liked_movie", methods = ["POST"])

def liked_movies():
     movie = details[0]
     details = details[1:]
     liked_movies.append(movie)
     return jsonify({
          "status": "success",
     }),201

@main.route("/not_liked_movie", methods = ["POST"])

def not_liked_movies():
     movie = details[0]
     details = details[1:]
     not_liked_movies.append(movie)
     return jsonify({
          "status": "success",
     }),201

@main.route("/not_watched_movie", methods = ["POST"])

def not_watched_movie():
     movie = details[0]
     details = details[1:]
     not_liked_movies.append(movie)
     return jsonify({
          "status": "success",
     }),201

if __name__ == "__main__":
     main.run()
