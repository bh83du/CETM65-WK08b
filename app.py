"""CETM65 - Week 8 - ePortfolio Task 2"""

import sqlite3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


# Create a new DB using SQL Alchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/portfolio.db'
db = SQLAlchemy(app)

# Define db table

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(6), unique = True, nullable = False)
    user_name = db.Column(db.String(50), unique = False, nullable = False)
    dept = db.Column(db.String(20), unique = False, nullable = True)
    password = db.Column(db.String(12))

# Define __repr__ method for the table

    def __repr__(self):
        user_repr = f"User ID: {self.user_id}" \
                    f"Name: {self.user_name}" \
                    f"Department: {self.dept}" \
                    f"Password: {self.password}" \

        return user_repr

# Add function for Route 'Sign-Up'

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        print(req)

        return redirect('/')

    return render_template('signup.html', title = 'Sign-Up')


app.run(debug=True)


