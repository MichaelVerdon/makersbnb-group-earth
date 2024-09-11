from routes.user_routes import *
from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository

'''
As an admin, I can send a #GET request
to see all the users
'''

# def test_get_all_users(web_client, db_connection):
#     db_connection.seed('seeds/makersbnb.sql')
#     response = web_client.get('/list_of_users')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'User(1, guest1@example.com, password1, guest1)\n' \
#                             'User(2, guest2@example.com, password2, guest2)\n' \
#                             'User(3, host1@example.com, password3, host1)\n' \
#                             'User(4, host2@example.com, password4, host2)'
    
'''
As a user, when I click the sign up button with my details
an account is created
'''

def test_sign_up_on_page(web_client, test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    connection = db_connection
    repo = UserRepository(connection)
    page.goto(f'http://{test_web_address}/create-account')
    page.fill("input[name='username']", 'test1')
    page.fill("input[name='password']", 'password1')
    page.fill("input[name='email']", 'user5@example.com')
    page.locator('.createaccount').click()
    assert repo.all() == [
        User(1, 'guest1@example.com', 'password1', 'guest1'),
        User(2, 'guest2@example.com', 'password2', 'guest2'),
        User(3, 'host1@example.com', 'password3', 'host1'),
        User(4, 'host2@example.com', 'password4', 'host2'),
        User(5, 'user5@example.com', 'password1', 'test1')
    ]

def test_account_exists_go_to_sign_in(web_client, test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/create-account')
    page.locator('.signin').click()
    h2 = page.locator('h2')
    expect(h2).to_have_text('Sign In')

def test_create_account_goes_to_sign_in(web_client, test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/create-account')
    page.fill("input[name='username']", 'test1')
    page.fill("input[name='password']", 'password1')
    page.fill("input[name='email']", 'user5@example.com')
    page.locator('.createaccount').click()
    h2 = page.locator('h2')
    expect(h2).to_have_text('Sign In')

def test_user_signs_in(web_client, test_web_address, db_connection, page: Page):
    # to set up session variables use the code below up to and including page.locator('.signin').click()
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    username_status_element = page.locator(".current_user_username")
    expect(username_status_element).to_have_text("guest1")

def test_user_signs_in_with_incorrect_email_but_correct_password(web_client, test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@exmple.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    sign_in_message = page.locator(".sign_in_message")
    expect(sign_in_message).to_have_text("Invalid email or password")

def test_user_signs_in_with_correct_email_incorrect_password(web_client, test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password')
    page.locator('.signin').click()
    sign_in_message = page.locator(".sign_in_message")
    expect(sign_in_message).to_have_text("Invalid email or password")









