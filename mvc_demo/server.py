from flask_app import app 
#one more line 
from flask_app.controllers import controller_users



#this need to be at the bottom 
if __name__=='__main__':
    app.run(debug=True)