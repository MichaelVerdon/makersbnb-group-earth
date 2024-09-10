from lib.booking import *

class BookingRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Retrieve all bookings
    def all(self):
        rows = self.db_connection.execute("SELECT * FROM bookings")
        return [Booking(row['id'], row['space_id'], row['user_id'], str(row['booking_date'])) for row in rows]
    
    # Retrieve all bookings a user has made
    def find_by_user(self, user_id):
        rows = self.db_connection.execute(f"SELECT * FROM bookings WHERE user_id = {user_id}")
        return [Booking(row['id'], row['space_id'], row['user_id'], str(row['booking_date'])) for row in rows]
    
    # To check all reservations for a space
    def find_bookings_by_place(self, space_id):
        rows = self.db_connection.execute(f"SELECT * FROM bookings WHERE space_id = {space_id}")
        return [Booking(row['id'], row['space_id'], row['user_id'], str(row['booking_date'])) for row in rows]
    
    def create_booking(self, space_id, user_id, booking_date):
        self.db_connection.execute(f"INSERT INTO bookings (space_id, user_id, booking_date) VALUES ({space_id}, {user_id}, '{booking_date}');")

    def remove_booking(self, space_id, user_id, booking_date):
        self.db_connection.execute\
        (f"DELETE FROM bookings WHERE space_id = {space_id} AND user_id = {user_id} AND booking_date = '{booking_date}'")