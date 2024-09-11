from lib.database_connection import get_flask_database_connection
from flask import request
from lib.space_repository import SpaceRepository
from lib.space import Space

# function to import the route in app.py
def apply_space_routes(app):   


    # POST /create-space
    # Creates a space
    
    @app.route('/create-space', methods=['POST'])
    def create_space():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space = Space(None, request.form['name'], request.form['description'], request.form['price_per_night'], request.form['availability_start'], request.form['availability_end'], request.form['user_id']) 
        space = repository.create(space)
        return "Space added successfully"
    
    # GET /all-spaces
    # Lists all spaces in the database

    @app.route('/all-spaces', methods=['GET'])
    def get_all_spaces():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        return "\n".join([
            str(space) for space in repository.all()
        ])
