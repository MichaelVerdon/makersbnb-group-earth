from lib.database_connection import get_flask_database_connection
from flask import request
from lib.space_repository import SpaceRepository
from lib.space import Space

# function to import the route in app.py
def apply_space_routes(app):   

    @app.route('/all-spaces', methods=['GET'])
    def get_all_spaces():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        return "\n".join([
            str(space) for space in repository.all()
        ])
