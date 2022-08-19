from flask import redirect, render_template, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE
from flask_app.models.model_user import User

@app.route('/')
def index():
    mysql = connectToMySQL(DATABASE)
    users = mysql.query_db('SELECT * FROM users;')
    return render_template('users.html', all_users=users)

@app.route('/user/new')
def new_user():
    return render_template('new_users.html')

@app.route('/user/<int:id>')
def show_user(id):
    user = User.get_user({'id': id})
    return render_template('show_users.html', users=user)

@app.route('/user/edit/<int:id>')
def edit_user(id):
    user = User.get_user({'id':id})
    return render_template('edit_users.html', users=user)


@app.route('/user/create', methods = ['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/user/update', methods=['POST'])
def update_user():
    User.update_user(request.form)
    return redirect('/')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_user({'id': id})
    return redirect('/')


#RESTful
#table_name/id (if possible)/ action

#2 types of routes -> Display routes and Action route
#user/new ->Display route: render the page that displats the form for a new user 
# user/create -> Action route: process the info from the user/new route and add to the database
# user/<int:id>-> Display route: show all the info of the table 
# user/<int:id>/edit-> DIsplay route: display the form in which you want to make the changes on 
# user/<int:id>/process-> Action route: proccess the info from the edit route
# user/<int:id>/delete-> Action route: delete record at id from your database 