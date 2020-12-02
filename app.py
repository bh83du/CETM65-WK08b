"""CETM65 - Week 8 - ePortfolio Task 2"""

import sqlite3
from Flask import flask, render_template, request, redirect
from flask_sqlachemy import SQLAlchemy
app = Flask(__name__)


# Create a new DB using SQL Alchemy

app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///data/portfolio.db'

# Define db table

class Users(db.model):
    user_id = db.Column(db.string(6), unique = True, nullable = False)
    user_name = db.Column(db.string(50), unique = False, nullable = False)
    dept = db.Column(db.string(20), unique = False, nullable = True)
    password = db.Column(db.string(12))


# Define __repr__ method for the table

    def __repr__(self)
        user_repr = f"User ID: {self.user_id}" \
                    f"Name: {self.user_name}" \
                    f"Department: {self.dept}" \
                    f"Password: {self.password}" \

        return user_repr

