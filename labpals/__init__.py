"""labpals package initializer."""
import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name

app.config.from_object("labpals.config")

app.config.from_envvar("LABPALS_SETTINGS", silent=True)

import labpals.model  # noqa: E402 pylint: disable=wrong-import-position
import labpals.utils  # noqa: E402 pylint: disable=wrong-import-position
import labpals.views  # noqa: E402 pylint: disable=wrong-import-position
import labpals.config
import labpals.api  # noqa: E402 pylint: disable=wrong-import-position