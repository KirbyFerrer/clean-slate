from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create
    @classmethod
    def create_user(cls, data):
        mysql = connectToMySQL(DATABASE)
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());'
        return mysql.query_db(query, data)

    # Get_one
    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])


    # Update_one
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        

    # Delete_one
    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users= []
        for user in results:
            all_users.append( cls(user) )
        return all_users

# create / save
# get_all
# get_one 
# update_one
# delete_one
