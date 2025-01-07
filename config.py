import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GOOEY_API_KEY = os.environ.get('GOOEY_API_KEY')
    DEBUG = True  # Enable debug mode