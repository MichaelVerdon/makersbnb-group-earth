from flask import Flask, request, app, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
import os

def get_user_routes(app):

    @app.route('/create-account', methods=['GET'])
    def get_login_page():
        return render_template('create_account.html')

    # @app.route('/list_of_users', methods=['GET'])
    # def get_list_of_users():
    #     connection = get_flask_database_connection(app)
    #     repo = UserRepository(connection)
    #     return '\n'.join(f'{user}' for user in repo.all())

    @app.route('/create-account', methods=['POST'])
    def sign_up_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        email = str(request.form['email'])
        password = str(request.form['password'])
        username = str(request.form['username'])
        repo.create(email, password, username)
        return redirect('/sign-in')

    @app.route('/sign-in', methods=['GET'])
    def get_signin_page():
        return render_template('sign_in.html')
    
    @app.route('/sign-in', methods=['POST'])
    def sign_in_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = str(request.form['username'])
        password = str(request.form['password'])
    
