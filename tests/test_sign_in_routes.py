from playwright.sync_api import Page, expect

def test_user_signs_in(test_web_address, db_connection, page: Page):
    # to set up session variables use the code below up to and including page.locator('.signin').click()
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    username_status_element = page.locator(".current_user_username")
    expect(username_status_element).to_have_text("guest1")


def test_user_signs_in_with_incorrect_email_but_correct_password(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@exmple.com')
    page.fill("input[name='password']", 'password1')
    page.locator('.signin').click()
    sign_in_message = page.locator(".sign_in_message")
    expect(sign_in_message).to_have_text("Invalid email or password")

def test_user_signs_in_with_correct_email_incorrect_password(test_web_address, db_connection, page: Page):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/sign-in')
    page.fill("input[name='email']", 'guest1@example.com')
    page.fill("input[name='password']", 'password')
    page.locator('.signin').click()
    sign_in_message = page.locator(".sign_in_message")
    expect(sign_in_message).to_have_text("Invalid email or password")
