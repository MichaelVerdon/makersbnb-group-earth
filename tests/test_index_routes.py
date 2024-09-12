

'''
When I am on the home page
I can click a button to get to my bookings
'''

def test_button_to_link_to_my_bookings(test_web_address, page):
    page.goto(f'http://{test_web_address}/index')
    page.locator('.mybookings').click()
    assert page.url == f'http://{test_web_address}/my-bookings'

'''
When I am on the home page
I can click a button to get to host listings
'''

def test_button_from_index_to_link_to_host_listings(test_web_address, page):
    page.goto(f'http://{test_web_address}/index')
    page.locator('.hostlistings').click()
    assert page.url == f'http://{test_web_address}/host-listings'