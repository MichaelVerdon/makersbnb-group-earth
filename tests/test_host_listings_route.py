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
    expect(page.locator('.name')).to_have_text('Name: Beach House')
    expect(page.locator('.description')).to_have_text('Description: A beautiful beach house with ocean view.')
    expect(page.locator('.price')).to_have_text('Price per Night: 150')
    expect(page.locator('.start')).to_have_text('Availability Start: 2024-09-15')
    expect(page.locator('.end')).to_have_text('Availability End: 2024-09-30')

"""
when user click on create space button it takes to a new page 
"""
def test_new_create_page(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('.createspace').click()
    expect(page.locator('.page-title')).to_have_text('Create new space')
"""
when the user  create a new space the new space is visible on the listings page 
"""

def test_user_create_space(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/create-space')
    page.fill("input[name='name']", 'testName')
    page.fill("input[name='description']", 'testDescription')
    page.fill("input[name='price_per_night']", 300)
    page.fill("input[name='availability_start ']", "2024-09-27")
    page.fill("input[name='availability_end']","2024-10-15")
    page.locator('.createspace').click()
    expect(page.locator('.name').nth(1)).to_have_text('Name: testName')
    expect(page.locator('.description').nth(1)).to_have_text('Description: testDescription')
    expect(page.locator('.price').nth(1)).to_have_text('Price per Night: 300')
    expect(page.locator('.start').nth(1)).to_have_text('Availability Start: 2024-09-27')
    expect(page.locator('.end').nth(1)).to_have_text('Availability End: 2024-10-15')
    
