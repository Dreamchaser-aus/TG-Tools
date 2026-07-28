from functools import wraps
from flask import session
from flask import redirect
from flask import url_for


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get("logged_in"):
            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return wrapper
