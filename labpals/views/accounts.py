import os
import hashlib
import uuid
import pathlib
from datetime import datetime
from werkzeug.exceptions import abort
import flask
import labpals
import labpals.utils
# from labpals.views import users

@labpals.app.route("/accounts/login/", methods=["GET", "POST"])
def login():
    """Login endpoint."""
    # print("in login line 57")
    if flask.session.get("username") is not None:
        return flask.redirect("/")

    if flask.request.method == "POST":
        pass
        # print("line 61 in login")
        # form = flask.request.form
        # username = form.get("username")
        # _password = form.get("password")
        # if username is None or _password is None:
        #     abort(400)
        # connection = insta485.model.get_db()
        # cur = connection.execute(
        #     "SELECT username, password " "FROM users " "WHERE username = ? ",
        #     [
        #         username,
        #     ],
        # )
        # rows = cur.fetchall()
        # if len(rows) == 0:
        #     abort(403)
        # for i in rows:
        #     salt = i["password"].split("$")
        #     salt = salt[1]
        #     _password = hash_with_salt(_password, salt)
        #     if _password != i["password"]:
        #         abort(403)
        #     # print("SIGNED IN: " + username)
        #     flask.session["username"] = username
        #     # return flask.redirect(flask.request.args.get('target'))
        #     return flask.redirect("/")

    return flask.render_template("accounts/login.html")