from flask import Flask,render_template,request,flash,redirect,url_for,session
from models import User,Category,Recipe

app = Flask(__name__)
USERS={}
def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if password == rpt_password:
            USERS[username] = User(name, username, password)
            return "Registration successful"
        return "Passwords don't match"    
    return "None input"

def login(username, password):
    """ Handles user login """
    if username and password:
        if USERS.get(username):
            if USERS[username].password == password:
                return "Login successful"
            return "Wrong password"
        return "User not found"   
    return "None input"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/sign_in", methods =['POST','GET'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        #creating an instance of the login fuction
        #creating an objetc return_value on our login function
        return_value = login(request.form['username'], request.form['password'])
        if return_value == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
        flash(return_value, 'warning')
    return render_template('login.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        #creating an instance of the register fuction
        return_value = register(request.form['name'], request.form['username'], request.form['password']
                          , request.form['rpt_password'])
        if return_value == "Registration successful":
            flash(return_value, 'info')
            return redirect(url_for('sign_in'))
        flash(return_value, 'warning')
    return render_template('register.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',categories=USERS[session['username']].categories)
@app.route('/add_category',methods = ['GET','POST'])
def add_category():
    if request.method == 'POST':
        return_value = USERS[session['username']].add_category(request.form('title'))
        if return_value =="recipe category is added succesfully":
            return redirect (url_for('dashboard'))
    return render_template('add category.html')
@app.route('/edit_category/<title>', methods = ['POST','GET'])
def edit_category(title):
    session['category_title'] = title
    if request.method =='POST':
        return_value = USERS[session['username']].edit_category(session[category_title],request.form(title))
        if return_value == "recipe_category edited succesfully":
            return redirect(url_for('dashboard'))
            flash (result, info)
    return render_template('edit_category.html')
@app.route('/delete/<title>', methods=['POST','GET'])
def delete_category(title):
    result = USERS[session['username']].delete_category(title)
    if result == "category deleted":
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('dashbord'))

if __name__ == '__main__':
    app.secret_key='sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)