from lib.user_repository import UserRepository
from lib.user import User

"""
When I call #all 
I get back list of users
"""

def test_all(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'guest1@example.com', 'password1', 'guest1'),
        User(2, 'guest2@example.com', 'password2', 'guest2'),
        User(3, 'host1@example.com', 'password3', 'host1'),
        User(4, 'host2@example.com', 'password4', 'host2')
    ]

"""
When I call #create on user_repository
I get a new user in database
"""

def test_create(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = UserRepository(db_connection)
    repository.create('user5@example.com', 'password5', 'guest3')
    assert repository.all() == [
        User(1, 'guest1@example.com', 'password1', 'guest1'),
        User(2, 'guest2@example.com', 'password2', 'guest2'),
        User(3, 'host1@example.com', 'password3', 'host1'),
        User(4, 'host2@example.com', 'password4', 'host2'),
        User(5,'user5@example.com', 'password5', 'guest3')
    ]

def test_get_with_id(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = UserRepository(db_connection)
    assert repository.get_by_id(2) == User(2, 'guest2@example.com', 'password2', 'guest2')