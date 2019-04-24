import os

SECRETE_KEY = os.getenv('SECRETE_KEY')
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DATABASE_NAME = os.environ['DATABASE_NAME']
DB_URI = 'postgresql://%s:%s@%s:5433/%s' %(DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=True
POSTGRES_ROOT_PASSWORD=os.environ['POSTGRES_ROOT_PASSWORD']
BLOG_NAME=os.environ['BLOG_NAME']
BLOG_POST_IMAGES_PATH=os.environ['BLOG_POST_IMAGES_PATH']