from flask import Flask, request, app, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.space import Space
from lib.booking_repository import BookingRepository
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
    
    @app.route("/update-space/<int:space_id>", methods=["GET"])
    def goto_update_space(space_id):
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space = repository.get_by_id(space_id)
        return render_template('update_space.html', space=space)
    
    @app.route("/update-space/<int:space_id>", methods=["POST"])
    def update_space(space_id):
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        name = request.form['name']
        description = request.form['description']
        price = request.form['price_per_night']
        start = request.form['availability_start']
        end = request.form['availability_end']

        space = repository.get_by_id(space_id)
        
        if end and start and end < start:
            return render_template('update_space.html', space=space, error="End date cannot be earlier than start date.")
        if end and end < space.availability_start:
            return render_template('update_space.html', space=space, error="End date cannot be earlier than start date.")
        if start and start > space.availability_end:
            return render_template('update_space.html', space=space, error="End date cannot be earlier than start date.")

        if name:
            repository.update_name(space_id, name)
        if description:
            repository.update_description(space_id, description)
        if price:
            repository.update_price_per_night(space_id, price)
        if start:
            repository.update_availability_start(space_id, start)
        if end:
            repository.update_availability_end(space_id, end)
        
        return redirect("/host-listings")
    

    @app.route("/delete-space/<int:space_id>", methods=["GET"])
    def delete_space(space_id):
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        repository.delete(space_id)
        return redirect("/host-listings")

    @app.route("/view-requests", methods=["GET"])
    def view_requests():
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        bookings_repository= BookingRepository(connection)
        spaces = space_repository.get_by_user_id(session["user_id"])
        bookings=[]
        for space in spaces:
            bookings.extend(bookings_repository.find_bookings_by_place(space.id))
        return render_template("view_requests.html", bookings=bookings)
