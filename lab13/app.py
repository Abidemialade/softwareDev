'''
Abidemi Alade
Lab13, Flask application
'''
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

''' create an object 'app' from the Flask module.
    __name__ set to __main__ if the script is running from the main file.
'''
app = Flask(__name__)
# connecting to PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:A1l2e3c4!@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create an object 'db' from the SQLAlchemy module
db = SQLAlchemy(app)

#create a secret key to handle data within our server
import os
app.config['SECRET_KEY'] = os.urandom(24)

#define a model (create table in the 'demoDB' database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

#define an employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        return 'Secessfullt requested! Enteres password = ' + request.form['password']
    name = "Abidemi"
    checkfruit = "kiwi"
    fruits = ['apple', 'banana', 'orange']
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']

            # Check if employee_id already exists
            existing_employee_id = Employee.query.filter_by(employee_id=emp_id).first()
            if existing_employee_id:
                flash(f"Error: Employee ID {emp_id} already exists!", 400)
            
                    # Check if employee_id already exists
            existing_employee_name = Employee.query.filter_by(employee_name=emp_name).first()
            if existing_employee_name:
                flash(f"Error: Employee ID {emp_name} already exists!", 400)

            # Create a new employee object and add form data to the database
            new_employee = Employee(employee_name=emp_name, employee_id=emp_id)

            # Remove the internal try/except block and let the external one handle failures
            db.session.add(new_employee)
            db.session.commit()

            # Store first employee name in session
            session['employee1'] = new_employee.employee_name

            # Message to be displayed after the employee is added to the database
            return f"{emp_name} added successfully!"
        except:
            flash("Failed to indert data! Try again")
        return render_template('users.html')


@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))
#set the 'app" to run if you execute the file directly(not when it is imported as a module)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)