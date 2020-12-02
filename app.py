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
    emp_no = db.Column(db.String(6), unique = True, nullable = False)
    user_name = db.Column(db.String(50), unique = False, nullable = False)
    dept = db.Column(db.String(20), unique = False, nullable = True)
    email = db.Column(db.String(60), unique = True, nullable = False)
    password = db.Column(db.String(30))

# Define __repr__ method for the table

    def __repr__(self):
        user_repr = f"ID: {self.id}" \
                    f"User ID: {self.emp_no}" \
                    f"Name: {self.user_name}" \
                    f"Department: {self.dept}" \
                    f"Email: {self.email}" \
                    f"Password: {self.password}" \

        return user_repr


# Add function for Default route

@app.route('/')
def data():
    all_users = Users.query.all() # Returns all records
    return render_template('data.html', all_users=all_users)

# Add function for Route 'Sign-Up'

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form

        new_user = Users(emp_no=req["emp_no"],
                         user_name=req["user_name"],
                         dept=req["dept"],
                         email=req["email"],
                         password=req["password"])

        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return redirect ('/')

    return render_template('signup.html', title = 'Sign-Up')


app.run(debug=True)