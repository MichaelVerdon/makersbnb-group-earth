from flask import Flask, request, app, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
import os
import sys

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
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        repo.create(email, password, username)
        return redirect('/sign-in')

    @app.route('/sign-in', methods=['GET'])
    def get_signin_page():
        return render_template('sign_in.html')
    
    @app.route('/sign-in', methods=['POST'])
    def sign_in_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        email = request.form['email']
        password = request.form['password']
        user = repo.verify_user(email, password)
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/index')
        else:
            return render_template('/sign_in.html', sign_in_message="Invalid email or password")
