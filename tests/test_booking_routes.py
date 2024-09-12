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

def test_get_booking_page(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    

    page.goto(f'http://{test_web_address}/create-booking?place_id=1')
    h1 = page.locator("h1")
    expect(h1).to_have_text("Beach House")
    p = page.locator('p')
    expect(p.nth(0)).to_have_text('A beautiful beach house with ocean view.')
    expect(p.nth(1)).to_have_text('Price-per-night: 150')
    expect(p.nth(2)).to_have_text('Available-from: 2024-09-15 to 2024-09-30')
    page.screenshot(path="screenshot.png", full_page=True)

def test_post_create_booking(test_web_address, db_connection, page: Page):
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest2@example.com')
    page.fill("input[name='password']", 'password2')
    page.locator('.signin').click()
    page.goto(f'http://{test_web_address}/create-booking?place_id=1')
    page.fill("input[name='booking-date']", '2024-09-21')
    page.locator('.submit-booking').click()
    p = page.locator(".details")
    page.screenshot(path="screenshot.png", full_page=True)
    expect(p).to_have_text("Beach House\n150")
    
