"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7m3m4dadc9vluhfq0-a.oregon-postgres.render.com",
        database="todo_c58v",
        user="todo_c58v_user",
        password="zjwKlq6nSKkxp5EULUtqzWYzI7EfriwB")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
