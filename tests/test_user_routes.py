from routes.user_routes import *
from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository

'''
As an admin, I can send a #GET request
to see all the users
'''

# def test_get_all_users(web_client, db_connection):
#     db_connection.seed('seeds/makersbnb.sql')
#     response = web_client.get('/list_of_users')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'User(1, guest1@example.com, password1, guest1)\n' \
#                             'User(2, guest2@example.com, password2, guest2)\n' \
#                             'User(3, host1@example.com, password3, host1)\n' \
#                             'User(4, host2@example.com, password4, host2)'
    








