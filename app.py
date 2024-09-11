import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from routes.user_routes import *

# Create a new Flask app
app = Flask(__name__)
app.secret_key = "psyducks_x_slowbros"
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    if 'username' in session:
        username = session['username']
    else:
        username = ""

    return render_template('index.html', username=username)

# imports space routes
from routes.space_routes import apply_space_routes
apply_space_routes (app)


get_user_routes(app)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
