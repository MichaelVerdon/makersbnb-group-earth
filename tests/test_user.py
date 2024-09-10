from lib.user import User

"""
When I construct a user it has a email, password 
and username.
"""

def test_construct():
    user = User(1, 'guest1@example.com', 'password1', 'guest1')
    assert user.id == 1
    assert user.email == 'guest1@example.com'
    assert user.password == 'password1'
    assert user.username == 'guest1'

"""
test equality
"""

def test_equality():
    user_1 = User(1, 'guest1@example.com', 'password1', 'guest1')
    user_2 = User(1, 'guest1@example.com', 'password1', 'guest1')
    assert user_1 == user_2

"""
test formatting.
"""

def test_stringifying():
    user = User(1, 'guest1@example.com', 'password1', 'guest1')
    assert str(user) == 'User(1, guest1@example.com, password1, guest1)'