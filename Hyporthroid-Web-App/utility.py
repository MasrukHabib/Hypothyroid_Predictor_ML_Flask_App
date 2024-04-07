from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import redirect, url_for, session, flash

db = SQLAlchemy()


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            # User is logged in, allow access to the route
            return route_function(*args, **kwargs)
        else:
            # User is not logged in, redirect to the login page
            flash('You need to log in to access this page.', 'warning')
            return redirect(url_for('login'))

    return wrapper
