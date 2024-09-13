import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from routes.user_routes import *
from routes.host_routes import *
from routes.booking_routes import *
from routes.sign_out_routes import *

# Create a new Flask app
app = Flask(__name__)
app.secret_key = "psyducks_x_slowbros"
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def create_session():
    session['username'] = None
    session['user_id'] = None

    return redirect('/index')



@app.route('/index', methods=['GET'])
def get_index():
    if 'username' in session:
        username = session['username']
    else:
        username = ""

    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()

    return render_template('index.html', username=username, spaces=spaces)

# imports space routes
from routes.space_routes import apply_space_routes
apply_space_routes (app)
get_user_routes(app)
get_host_routes(app)
apply_booking_routes(app)
apply_sign_out_route(app)
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

