from playwright.sync_api import Page, expect

def test_view_bookings(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()

    page.goto(f'http://{test_web_address}/my-bookings')
    
    p_list = page.locator(".date")
    
    expect(p_list.nth(0)).to_have_text("2024-09-20")
    expect(p_list.nth(1)).to_have_text("2024-11-11")

def test_view_bookings_with_details(test_web_address, db_connection, page: Page):

    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()

    page.goto(f'http://{test_web_address}/my-bookings')
    
    p_list = page.locator(".details")

    page.screenshot(path="screenshot.png", full_page=True)
    expect(p_list.nth(0)).to_have_text("Beach House\n150")
    expect(p_list.nth(1)).to_have_text("Mountain Cabin\n120")

'''
As a user on the my booking page
I can click on a homepage button
so that I go back to the homepage
'''

def test_button_from_my_bookings_to_homepage(test_web_address, page):
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/my-bookings')
    page.locator('.homepage').click()
    assert page.url == f'http://{test_web_address}/index'