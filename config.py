import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost/alchemy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
