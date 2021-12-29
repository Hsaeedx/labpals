import os
import hashlib
import uuid
import pathlib
from datetime import datetime
from werkzeug.exceptions import abort
import flask

import labpals

def execute_query(query, *arguments):
    """Execute a query on the DB with given arguments."""
    _db = labpals.model.get_db()
    cursor = _db.execute(query, arguments)
    rows = cursor.fetchall()
    return rows