from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import User, Recipe

app = Flask(__name__)
USERS = {}


def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if password == rpt_password:
            USERS[username] = User(name, username, password)
            return True
        return False
    return False


def login(username, password):
    """ Handles user login """
    if username and password:
        if USERS.get(username):
            if USERS[username].password == password:
                return False
            return False
        return False
    return False


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/sign_in", methods=['POST', 'GET'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        return_value = login(
            request.form['username'], request.form['password'])
        if return_value == True:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
        flash("Login successful", 'warning')
    return render_template('login.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        # creating an instance of the register fuction
        return_value = register(request.form['name'], request.form['username'],
                                request.form['password'], request.form['rpt_password'])
        if return_value == True:
            return redirect(url_for('sign_in'))
        flash("Login successful", 'warning')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_category():

    return render_template('add category.html')


@app.route('/edit_recipe/<title>', methods=['POST', 'GET'])
def edit_category(title):

    return render_template('edit_category.html')


@app.route('/delete/<title>', methods=['POST', 'GET'])
def delete_category(title):

    return redirect(url_for('dashbord'))


if __name__ == '__main__':
    app.secret_key = 'sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)
