"""labpals_app index (main) view.

URLs include: /
"""
import os
import flask
import arrow
import labpals

@labpals.app.route("/")
def show_index():
    """Display / route."""
    context = {"obama": 1}
    logged_in_user = flask.session.get('username')

    # if logged_in_user is None:
    #     return flask.redirect(flask.url_for("login"))

    return flask.render_template("index.html", **context)


@labpals.app.route("/favicon.ico")
def favicon():
    """Return our favicon."""
    return flask.send_from_directory(
        os.path.join(labpals.app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )