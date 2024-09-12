from lib.space import Space
from lib.space_repository import SpaceRepository


#Test that we are getting the list of all spaces of the database
def test_return_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result == [
                    Space(1, 'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3),
                    Space(2, 'Tree House', 'A house my dad build in my backyard', 125, '2024-10-11', '2024-11-30', 1),
                    Space(3, 'Mountain Cabin', 'A cozy cabin in the mountains.', 120, '2024-10-01', '2024-10-15', 4)
                    ]

#test to see if the function to create a space is working
def test_create_a_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    created_space = repository.create(Space(4,'Castle', 'A lovely castle.', 500, '2024-12-25', '2024-12-27', 2))
    assert created_space == Space(4,'Castle', 'A lovely castle.', 500, '2024-12-25', '2024-12-27', 2)

    result = repository.all()
    assert result == [
        Space(1, 'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3),
        Space(2, 'Tree House', 'A house my dad build in my backyard', 125, '2024-10-11', '2024-11-30', 1),
        Space(3, 'Mountain Cabin', 'A cozy cabin in the mountains.', 120, '2024-10-01', '2024-10-15', 4),
        Space(4, 'Castle', 'A lovely castle.', 500, '2024-12-25', '2024-12-27', 2)
    ]

def test_get_space_by_user_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.get_by_user_id(3)
    assert result == [
        Space(1, 'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)
    ]
def test_get_place_details_by_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.get_by_id(1)
    assert result == Space(1, 'Beach House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)


"""
given a space name the host can update the space name

"""

def test_update_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.update_name('Beach House', 'Lake House')
    assert repository.get_by_id(1)== Space(1, 'Lake House', 'A beautiful beach house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)

    repository.update_description('Lake House', 'A beautiful lake house with ocean view.')
    assert repository.get_by_id(1)== Space(1, 'Lake House', 'A beautiful lake house with ocean view.', 150, '2024-09-15', '2024-09-30', 3)

    repository.update_price_per_night('Lake House', 300)
    assert repository.get_by_id(1)== Space(1, 'Lake House', 'A beautiful lake house with ocean view.', 300, '2024-09-15', '2024-09-30', 3)

    repository.update_availability_start('Lake House', '2024-09-25')
    assert repository.get_by_id(1)== Space(1, 'Lake House', 'A beautiful lake house with ocean view.', 300, '2024-09-25', '2024-09-30', 3)

    repository.update_availability_end('Lake House', '2024-10-11')
    assert repository.get_by_id(1)== Space(1, 'Lake House', 'A beautiful lake house with ocean view.', 300, '2024-09-25', '2024-10-11', 3)
