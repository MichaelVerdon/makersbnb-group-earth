from flask import Flask, request, app, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
import os
import sys
from lib.booking_repository import *
from lib.booking import *
from lib.space_repository import *
from lib.space import *
import re
import datetime

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
    

    @app.route('/create-booking', methods=["GET"])
    def get_create_booking():
        place_id = request.args['place_id']
        repo = SpaceRepository(get_flask_database_connection(app))
        place = repo.get_by_id(place_id)
        return render_template('create_booking.html', place=place)


    @app.route('/create-booking', methods=["POST"])
    def submit_create_booking():
        booking_repo = BookingRepository(get_flask_database_connection(app))
        space_repo = SpaceRepository(get_flask_database_connection(app))
        place_id = request.form['place_id']
        booking_date = request.form['booking-date']
        place = space_repo.get_by_id(place_id)

        # Check its in format YYYY-MM-DD
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', booking_date):
            return render_template('create_booking.html', place=place, error_message="Please input a valid date!")
        
        # Check existing bookings for the place and if the date is already booked in.
        bookings = booking_repo.find_bookings_by_place(place_id)
        for booking in bookings:
            if booking.booking_date == booking_date:
                return render_template('create_booking.html', \
                place=place, error_message="Date already booked by someone else!")
            
        # start_date, end_date, set_date = datetime.strptime(place.availability_start, '%m-%d-%Y').date(),\
        #     datetime.strptime(place.availability_end, '%m-%d-%Y').date(), datetime.strptime(set_date, '%m-%d-%Y').date()

        # if set_date > end_date or set_date < start_date:
        #     return render_template('create_booking.html', \
        #         place=place, error_message="Date is not in availability range!")

        booking_repo.create_booking(place_id, session["user_id"], booking_date)

        return redirect('/my-bookings')
