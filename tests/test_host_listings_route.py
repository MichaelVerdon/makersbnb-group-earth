from routes.user_routes import *
from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository

"""
When a host signs in and goes to their listings
They can see all of their spaces
"""

def test_show_spaces_for_host(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.screenshot(path='screenshot.png', full_page=True)
    expect(page.locator('.name')).to_have_text('Name: Beach House')
    expect(page.locator('.description')).to_have_text('Description: A beautiful beach house with ocean view.')
    expect(page.locator('.price')).to_have_text('Price per Night: 150')
    expect(page.locator('.start')).to_have_text('Availability Start: 2024-09-15')
    expect(page.locator('.end')).to_have_text('Availability End: 2024-09-30')

