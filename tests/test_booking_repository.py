from lib.booking_repository import *
from lib.booking import *

def test_repo_all(db_connection):
    db_connection.seed("./seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    assert repo.all() == [
        Booking(1, 1, 1, '2024-09-20'),
        Booking(2, 2, 2, '2024-10-10'),
        Booking(3, 3, 1, '2024-11-11')
    ]

# Allow a user to see all bookings they made
def test_find_booking_by_user(db_connection):
    db_connection.seed("./seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    assert repo.find_by_user(2) == [Booking(2, 2, 2, '2024-10-10')]

# To find bookings in a place a user is viewing
def test_find_by_place_id(db_connection):
    db_connection.seed("./seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    assert repo.find_bookings_by_place(1) == [Booking(1, 1, 1, '2024-09-20')]

def test_create_booking(db_connection):
    db_connection.seed("./seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    repo.create_booking(1, 2, '2024-09-29')
    assert repo.all()[-1] == Booking(4, 1, 2, '2024-09-29')

def test_remove_booking(db_connection):
    db_connection.seed("./seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    repo.remove_booking(1, 1, '2024-09-20')
    assert repo.all() == [
        Booking(2, 2, 2, '2024-10-10'),
        Booking(3, 3, 1, '2024-11-11')
    ]