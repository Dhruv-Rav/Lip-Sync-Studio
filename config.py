import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GOOEY_API_KEY = sk-C1WwUld5GRchdHz7nVM2oBx0dGwaRKH0j0MOxxA6od56YnIr
    DEBUG = True  # Enable debug mode
