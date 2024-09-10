from routes.sign_up import *
from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository

'''
As an admin, I can send a #GET request
to see all the users
'''

def test_get_all_users(web_client, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    response = web_client.get('/list_of_users')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'User(1, guest1@example.com, password1, guest1)\n' \
                            'User(2, guest2@example.com, password2, guest2)\n' \
                            'User(3, host1@example.com, password3, host1)\n' \
                            'User(4, host2@example.com, password4, host2)'
    

def test_sign_up_with_details(web_client, test_web_address, db_connection, page):
    db_connection.seed('seeds/makersbnb.sql')
    connection = db_connection
    repo = UserRepository(connection)
    response = web_client.post('/login', data={
        'username': 'test1',
        'password': 'password1',
        'email': 'user5@example.com'
    })
    assert response.status_code == 201
    users = repo.all()
    assert users == [
        User(1, 'guest1@example.com', 'password1', 'guest1'),
        User(2, 'guest2@example.com', 'password2', 'guest2'),
        User(3, 'host1@example.com', 'password3', 'host1'),
        User(4, 'host2@example.com', 'password4', 'host2'),
        User(5, 'user5@example.com', 'password1', 'test1')  # Ensure the new user is here
    ]


'''
As a user, when I click the sign up button with my details
an account is created
'''

def test_sign_up_with_details(web_client, test_web_address, db_connection, page):
    db_connection.seed('seeds/makersbnb.sql')
    connection = db_connection
    repo = UserRepository(connection)
    page.goto(f'http://{test_web_address}/login')
    page.fill("input[name='username']", 'test1')
    page.fill("input[name='password']", 'password1')
    page.fill("input[name='email']", 'user5@example.com')
    page.click('text = Create Account')
    assert get_user_routes.sign_up_user() == [
        User(1, 'guest1@example.com', 'password1', 'guest1'),
        User(2, 'guest2@example.com', 'password2', 'guest2'),
        User(3, 'host1@example.com', 'password3', 'host1'),
        User(4, 'host2@example.com', 'password4', 'host2'),
        User(5, 'user5@example.com', 'password1', 'test1')
    ]



