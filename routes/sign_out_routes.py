from flask import redirect, session, url_for

def apply_sign_out_route(app):

    @app.route('/sign-out')
    def sign_out():
        session['user_id'] = None
        session['username'] = None

        return redirect('/sign-in')