from playwright.sync_api import Page, expect
from flask import session

'''
When I'm signed in on the index page
I can click the sign out button
and be signed out and redirected to the sign in page
'''

def test_sign_out_button_from_index_page(test_web_address, db_connection, page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.locator('.signed-in-status').click()
    assert page.url == f'http://{test_web_address}/sign-in'
