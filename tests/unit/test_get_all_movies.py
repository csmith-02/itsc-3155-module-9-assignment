from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies():
    # Get the movie repository
    singleton = get_movie_repository()
    singleton.clear_db()

    # Add a movie to the repository and check if the length of the all_movies dictionary is 1
    movie1 = singleton.create_movie('Test', 'Doug', '3')
    movies = singleton.get_all_movies()
    assert len(movies) == 1

    # Add two more movies to test length one more time
    movie2 = singleton.create_movie('Test', 'Sam', '1')
    movie3 = singleton.create_movie('Test', 'Andrew', '4')
    movies = singleton.get_all_movies()
    assert len(movies) == 3

    # Delete the three movies and check that the length is 0
    singleton.delete_movie(movie1.movie_id)
    singleton.delete_movie(movie2.movie_id)
    singleton.delete_movie(movie3.movie_id)
    movies = singleton.get_all_movies()
    assert len(movies) == 0