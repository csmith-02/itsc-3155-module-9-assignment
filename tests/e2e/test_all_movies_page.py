from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_all_movies_page(test_app: FlaskClient):
    
    # Test that the route loads with a 200 success status_code
    assert test_app.get('/movies').status_code == 200
    
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')

    # Test App Client with zero movies created and added
    singleton = get_movie_repository()
    assert '<h1>You have not created any movie ratings!</h1>' in data

    # Create new movie for database
    movie1 = singleton.create_movie('Clash of Titans', 'Connor Smith', 3)

    # Test to make sure h1 tag "You have no created any movie ratings!" is no longer in the HTML after adding the movie
    response = test_app.get('/movies')
    data = response.data.decode()
    assert '<h1>You have not created any movie ratings!</h1>' not in data

    # assert that a table now exists for the newly added movie
    assert '<table ' in data

    # Test to make sure when the movie is removed, and the h1 tag "You have no created any movie ratings!" returns
    # Test to ensure table is no longer showing
    singleton.delete_movie(movie1.movie_id)
    response = test_app.get('/movies')
    data = response.data.decode()

    assert '<table ' not in data
    assert '<h1>You have not created any movie ratings!</h1>' in data



