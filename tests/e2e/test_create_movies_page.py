from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_create_movies_page(test_app: FlaskClient):
    
    # Test that the route loads with a 200 success status_code
    assert test_app.get('/movies/new').status_code == 200

    # Test page loaded correctly
    response = test_app.get('/movies/new')
    data = response.data.decode()

    assert '<h1 class="mb-5">Create Movie Rating</h1>' in data
    assert '<p class="mb-3">Create a movie rating below</p>' in data
    assert '<form action = "/movies" method="POST">' in data

    # Test form bad request
    response = test_app.post('/movies', data={}, follow_redirects=True)
    assert response.status_code == 400

    # Test successfully creating a movie review and redirecting to movie list page
    singleton = get_movie_repository()
    singleton.clear_db()
    response = test_app.post('/movies', data={'title': 'Test-movie', 'director': 'Test-director', 'rating': '5'}, follow_redirects=True)
    data = response.data.decode()

    assert response.status_code == 200
    assert 'Test-movie' in data
    assert 'Test-director' in data
    assert '5' in data
