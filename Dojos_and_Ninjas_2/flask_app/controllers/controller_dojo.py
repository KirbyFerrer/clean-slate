from flask_app import app
from flask import render_template, request, redirect 
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

# -----Display routes -----

@app.route('/dojos')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('home.html', all_dojos = dojos)

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id': id 
    }
    dojo = Dojo.get.dojo_ninjas(data)
    return render_template('show_dojo.html', dojos=dojo)

# ----- Action routes -----

@app.route('dojos/create', methods = ['POST'])
def create_dojo():
    Dojo.create_dojo(request.from)
    return redirect('/dojos')
