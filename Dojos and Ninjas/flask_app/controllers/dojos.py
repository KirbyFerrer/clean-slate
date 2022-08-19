from flask import redirect, render_template, request
# from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja 

# ------------Display routes--------------

@app.route('/dojos')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("home.html", all_dojos = dojos)

@app.route('/dojos/<int:id>') #will show user info when 'view' is selected
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_ninjas(data)
    return render_template("show_dojo.html", dojos=dojo)

# # ----------action routes (behind the scenes)-----------

@app.route('/dojos/create', methods = ["POST"]) #route that user sends data too
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')