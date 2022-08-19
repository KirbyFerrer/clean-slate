from flask import redirect, render_template, request
# from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# ------------Display routes--------------

@app.route('/ninjas') #displays new ninja form 
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("create_ninja.html", dojos = dojos)



# # ----------action routes (behind the scenes)-----------

@app.route('/ninjas/create', methods = ["POST"]) #route that user sends data too
def create_ninja():
    Ninja.create(request.form)
    return redirect('/dojos')
