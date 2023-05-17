"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7md64dadc9vlumar0-a.oregon-postgres.render.com",
        database="todo_w249",
        user="root",
        password="vFAjrh2yXABAHehUaBhH9KDGj3JIUPdZ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
