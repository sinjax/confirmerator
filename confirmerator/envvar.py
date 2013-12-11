import os
DEBUG = os.environ.get('DEBUG', False) == "1"
SECRET_KEY = os.environ.get('SECRECT',"notsecret")
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',"sqlite:///test.db")