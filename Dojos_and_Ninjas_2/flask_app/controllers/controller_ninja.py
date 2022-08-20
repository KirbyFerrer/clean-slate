from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja 

# ----- Display routes -----

@app.route('ninjas')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('create_ninja.html', dojos = dojos)

# ----- Action route -----

@app.route('/ninjas/create', methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/dojos')

