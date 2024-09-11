from flask import Flask, request, app, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
import os
import sys
from lib.booking_repository import *
from lib.booking import *
from lib.space_repository import *
from lib.space import *

def apply_booking_routes(app):

    @app.route('/my-bookings', methods=["GET"])
    def get_my_bookings():
        booking_repo = BookingRepository(get_flask_database_connection(app))
        space_repo = SpaceRepository(get_flask_database_connection(app))
        my_bookings = booking_repo.find_by_user(session["user_id"])
        bookings = []
        for booking in my_bookings:
            space = space_repo.get_by_id(booking.space_id)
            details = booking_repo.get_booking_details(space)
            to_add = {
                "date":booking.booking_date,
                "name":details["name"],
                "price":details["price"]
            }
            bookings.append(to_add)

        return render_template('/my_bookings.html', bookings=bookings)