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
    expect(page.locator('#name')).to_have_text('Name: Beach House')
    expect(page.locator('#description')).to_have_text('Description: A beautiful beach house with ocean view.')
    expect(page.locator('#price')).to_have_text('Price per Night: 150')
    expect(page.locator('#start')).to_have_text('Availability Start: 2024-09-15')
    expect(page.locator('#end')).to_have_text('Availability End: 2024-09-30')

'''
When I am on listings, 
I can go back to index 
by clicking on a homepage button
'''

def test_button_from_host_listing_to_hompage(test_web_address, page):
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill('input[name="email"]', 'guest1@example.com')
    page.fill('input[name="password"]', 'password1')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('.homepage').click()
    assert page.url == f'http://{test_web_address}/index'

'''
When I am on my listings (/host-listings)
I can click a my listings button 
so that I can get to my listings
'''

def test_button_to_link_to_my_bookings(test_web_address, page):
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill('input[name="email"]', 'guest1@example.com')
    page.fill('input[name="password"]', 'password1')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('.mybookings').click()
    assert page.url == f'http://{test_web_address}/my-bookings'
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
    page.locator('#createspace').click()
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
    page.fill("input[name='price_per_night']", "300")
    page.fill("input[name='availability_start']", "2024-09-27")
    page.fill("input[name='availability_end']","2024-10-15")
    page.locator('#createspace').click()
    expect(page.locator('#name').nth(1)).to_have_text('Name: testName')
    expect(page.locator('#description').nth(1)).to_have_text('Description: testDescription')
    expect(page.locator('#price').nth(1)).to_have_text('Price per Night: 300')
    expect(page.locator('#start').nth(1)).to_have_text('Availability Start: 2024-09-27')
    expect(page.locator('#end').nth(1)).to_have_text('Availability End: 2024-10-15')

def test_user_updates_space_name(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    page.screenshot(path='screenshot.png', full_page=True)
    expect(page.locator('#name')).to_have_text('Beach House')
    page.fill("input[name='name']", 'Lake House')
    page.locator('#update').click()
    expect(page.locator('#name').nth(0)).to_have_text('Name: Lake House')

def test_user_updates_with_empty_field(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#name')).to_have_text('Beach House')
    page.locator('#update').click()
    expect(page.locator('#name').nth(0)).to_have_text('Name: Beach House')

def test_user_updates_space_description(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#description')).to_have_text('A beautiful beach house with ocean view.')
    page.fill("input[name='description']", 'A beautiful lake house with lake view.')
    page.locator('#update').click()
    expect(page.locator('#description').nth(0)).to_have_text('Description: A beautiful lake house with lake view.')

def test_user_updates_space_price(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#price')).to_have_text('150')
    page.fill("input[name='price_per_night']", '300')
    page.locator('#update').click()
    expect(page.locator('#price').nth(0)).to_have_text('Price per Night: 300')

def test_user_updates_space_availability_start(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#availability_start')).to_have_text('2024-09-15')
    page.fill("input[name='availability_start']", '2024-09-29')
    page.locator('#update').click()
    expect(page.locator('#start').nth(0)).to_have_text('Availability Start: 2024-09-29')

def test_user_updates_space_availability_end(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#availability_end')).to_have_text('2024-09-30')
    page.fill("input[name='availability_end']", '2024-10-15')
    page.locator('#update').click()
    expect(page.locator('#end').nth(0)).to_have_text('Availability End: 2024-10-15')

"""
When a user tries to update the end so its before the start date, they get an error
"""

def test_user_updates_space_availability_end_when_end_is_before_start(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#availability_end')).to_have_text('2024-09-30')
    page.fill("input[name='availability_end']", '2024-08-15')
    page.locator('#update').click()
    expect(page.locator('#errormessage')).to_have_text("End date cannot be earlier than start date.")

"""
When a user tries to update the start so its after the end date, they get an error
"""

def test_user_updates_space_availability_start_when_start_is_after_end(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#update_1').click()
    expect(page.locator('#availability_start')).to_have_text('2024-09-15')
    page.fill("input[name='availability_start']", '2024-10-29')
    page.locator('#update').click()
    expect(page.locator('#errormessage')).to_have_text("End date cannot be earlier than start date.")

"""
When I delete a space it is no longer visible
"""
def test_user_delete_space(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'host1@example.com')
    page.fill("input[name='password']", 'password3')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/host-listings')
    page.locator('#delete_1').click()
    expect(page.locator('h2')).to_have_text('Your Listings')
    expect(page.locator('#name')).to_have_count(0)

