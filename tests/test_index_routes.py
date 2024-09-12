from playwright.sync_api import expect

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

'''
When I am on the homepage #index I 
see all the spaces available listed
'''

def test_homepage_has_all_spaces_listed(test_web_address, page, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f'http://{test_web_address}/index')
#space 1: Beach House
    expect(page.locator('#name1')).to_have_text('Name: Beach House')
    expect(page.locator('#description1')).to_have_text('Description: A beautiful beach house with ocean view.')
    expect(page.locator('#price1')).to_have_text('Price per Night: 150')
    expect(page.locator('#start1')).to_have_text('Availability Start: 2024-09-15')
    expect(page.locator('#end1')).to_have_text('Availability End: 2024-09-30')
#space 2: Tree House
    expect(page.locator('#name2')).to_have_text('Name: Tree House')
    expect(page.locator('#description2')).to_have_text('Description: A house my dad build in my backyard.')
    expect(page.locator('#price2')).to_have_text('Price per Night: 125')
    expect(page.locator('#start2')).to_have_text('Availability Start: 2024-10-11')
    expect(page.locator('#end2')).to_have_text('Availability End: 2024-11-30')
#space 3: Mountain Cabin
    expect(page.locator('#name3')).to_have_text('Name: Mountain Cabin')
    expect(page.locator('#description3')).to_have_text('Description: A cozy cabin in the mountains.')
    expect(page.locator('#price3')).to_have_text('Price per Night: 120')
    expect(page.locator('#start3')).to_have_text('Availability Start: 2024-10-01')
    expect(page.locator('#end3')).to_have_text('Availability End: 2024-10-15')
