from flask import Flask
from flask_restful import Resource, Api
import csv

import models

app = Flask(__name__)
api = Api(app)

class Links(Resource):
    def get(self):
        path = r'Movies_data/links.csv'
        links = []
        with open(path, newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            data = list(reader)
        for i, _ in enumerate(data):
            links.append(models.Link(data[i][0], data[i][1], data[i][2]).__dict__)
    
        return links

class Movies(Resource):
    def get(self):
        path = r'Movies_data/movies.csv'
        movies = []
        with open(path, newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            data = list(reader)
        for i, _ in enumerate(data):
            movies.append(models.Movie(data[i][0], data[i][1], data[i][2]).__dict__)
    
        return movies


class Ratings(Resource):
    def get(self):
        path = r'Movies_data/ratings.csv'
        ratings = []
        with open(path, newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            data = list(reader)
        for i, _ in enumerate(data):
            ratings.append(models.Rating(data[i][0], data[i][1], data[i][2], data[i][3]).__dict__)
    
        return ratings


class Tags(Resource):
    def get(self):
        path = r'Movies_data/tags.csv'
        tags = []
        with open(path, newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile, delimiter =',')
            data = list(reader)
        for i, _ in enumerate(data):
            tags.append(models.Tag(data[i][0], data[i][1], data[i][2], data[i][3]).__dict__)
    
        return tags


api.add_resource(Links, '/links')
api.add_resource(Movies, '/movies')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
