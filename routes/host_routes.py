from flask import Flask, request, app, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.space import Space
import os
import sys


def get_host_routes(app):

    @app.route("/host-listings", methods=["GET"])
    def get_host_listings_page():
        # shows all listings for signed in host
        user_id = session["user_id"]
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        spaces = repository.get_by_user_id(user_id)

        return render_template("host_listings.html", spaces=spaces)

    @app.route("/create-space", methods=["GET"])
    def get_new_space_page():
        return render_template("create_space.html")

    @app.route("/create-space", methods=["POST"])
    def create_new_space():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space = Space(
            None,
            request.form["name"],
            request.form["description"],
            request.form["price_per_night"],
            request.form["availability_start"],
            request.form["availability_end"],
            session['user_id'],
        )
        space = repository.create(space)
        return redirect("/host-listings")