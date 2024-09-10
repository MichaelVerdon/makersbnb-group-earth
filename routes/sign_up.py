from flask import Flask, request, app, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
import os

def get_user_routes(app):

    @app.route('/login', methods=['GET'])
    def get_login_page():
        return render_template('login.html')

    @app.route('/list_of_users', methods=['GET'])
    def get_list_of_users():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        return '\n'.join(f'{user}' for user in repo.all())

    @app.route('/login', methods=['POST'])
    def sign_up_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        repo.create(request.form['email'], request.form['password'], request.form['username'])
        return repo.all(), 201
