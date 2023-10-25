from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    # Get the movie repository
    singleton = get_movie_repository()
    singleton.clear_db()

    #Create movie and test to see if created successfully
    movie1 = singleton.create_movie('Test-movie', 'Test-director', '5')
    assert movie1.title == 'Test-movie'
    assert movie1.director == 'Test-director'
    assert movie1.rating == '5'

