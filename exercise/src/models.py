# TODO - Create SQLAlchemy DB and Movie model
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    director = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(255), nullable=False)

    def __init__(self, title: str, director: str, rating: int):
        self.title = title
        self.rating = rating
        self.director = director

    def __repr__(self):
        return '<Movie %r>' % self.movie_id

    


