from lib2to3.pytree import _Results
from unittest import result
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        mysql = connectToMySQL(DATABASE)
        query = 'INSERT INTO dojos (name) VALUES(%(name)s);'
        return mysql.query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        mysql = connectToMySQL(DATABASE)
        results = mysql.query_db('SELECT * FROM dojos;')
        all_dojos = []
        if results:
            for row in results:
                all_dojos.append(cls(row))
            return all_dojos

    @classmethod
    def get_dojo(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s ;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) == 0:
            return 'No Ninjas Found'
        dojo = cls(results[0])
        if results:
            for row in results:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at'],
                    'dojo_id': row['dojo_id']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
            return dojo
