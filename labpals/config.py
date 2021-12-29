"""Labpals development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xde\x83\xb0\x87\xa4\x01b\x03\xdf\x12i\xa5\xf7\x8fJ\xe7R\x01\r\xdd\xc8\xcbZ\x92'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
LABPALS_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = LABPALS_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/labpals.sqlite3
DATABASE_FILENAME = LABPALS_ROOT/'var'/'labpals.sqlite3'
