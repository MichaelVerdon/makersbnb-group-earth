class Booking:
    def __init__(self, id, space_id, user_id, booking_date):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.booking_date = booking_date

    def __repr__(self):
        return f"Booking({self.id}, {self.space_id}, {self.user_id}, {self.booking_date})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # This will be used for checking if a booking with a date exists
    # This can be done by looping through all booking objects in repo.all()
    # and then calling this method for each item in the database.
    def date_taken(self, new_booking_date):
        return self.booking_date == new_booking_date