from lib.booking import *

# Test class initialisation
def test_booking_init():
    booking = Booking(1, 5, 3, '2024-09-20')
    assert booking.id == 1
    assert booking.space_id == 5
    assert booking.user_id == 3
    assert booking.booking_date == '2024-09-20'

# Test toString method
def test_repr():
    booking = Booking(1, 5, 3, '2024-09-20')
    assert str(booking) == 'Booking(1, 5, 3, 2024-09-20)'

# Test equals method
def test_eq():
    booking1 = Booking(1, 5, 3, '2024-09-20')
    booking2 = Booking(1, 5, 3, '2024-09-20')
    assert booking1 == booking2

# Test if two dates match which will be useful for booking later.
def test_date_taken():
    booking = Booking(1, 5, 3, '2024-09-20')
    assert booking.date_taken('2024-09-20') == True
    assert booking.date_taken('2024-09-25') == False
