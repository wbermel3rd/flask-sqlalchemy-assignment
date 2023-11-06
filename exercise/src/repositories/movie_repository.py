from ..models import db, Movie

class MovieRepository:
 
    def get_all_movies(self):
        movies = Movie.query.all() 
        return movies

    def get_movie_by_id(self, fmovie_id):
        movie =  Movie.query.filter_by(movie_id=fmovie_id).first()
        return movie

    def create_movie(self, title, director, rating):
        new_movie = Movie(title, director, rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        movies = Movie.query.filter(Movie.title.like(f"%{title}%")).all()
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return movies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
