from lib.user_repository import UserRepository
from lib.user import User
from playwright.sync_api import Page, expect

'''
As a user, when I click the sign up button with my details
an account is created
'''

def test_sign_up_on_page(test_web_address, db_connection, page: Page):
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

def test_account_exists_go_to_sign_in(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/create-account')
    page.locator('.signin').click()
    h2 = page.locator('h2')
    expect(h2).to_have_text('Sign In')

'''
When I sucessfully create an account
I am then redirected to the sign in page
'''

def test_create_account_goes_to_sign_in(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/create-account')
    page.fill("input[name='username']", 'test1')
    page.fill("input[name='password']", 'password1')
    page.fill("input[name='email']", 'user5@example.com')
    page.locator('.createaccount').click()
    h2 = page.locator('h2')
    expect(h2).to_have_text('Sign In')

'''
When I already have an account and I'm on the create account page
I can click a button to take me to the sign in page
'''

def test_button_to_redirect_to_sign_in_page(test_web_address, page):
    page.goto(f'http://{test_web_address}/create-account')
    page.locator('.signin').click()
    assert page.url == f'http://{test_web_address}/sign-in'


'''
As a user on the create account page
I can click on a homepage button
so that I go back to the homepage
'''

def test_button_from_redirect_to_homepage(test_web_address, page):
    page.goto(f'http://{test_web_address}/create-account')
    page.locator('.homepage').click()
    assert page.url == f'http://{test_web_address}/index'
