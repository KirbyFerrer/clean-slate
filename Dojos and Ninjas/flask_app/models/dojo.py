from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import ninja 

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        mysql = connectToMySQL("dojos_and_ninjas_db")
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        return mysql.query_db(query, data) #return the id of user created

    @classmethod
    def get_all_dojos(cls):
        mysql = connectToMySQL("dojos_and_ninjas_db") #how we connect to DB
        results = mysql.query_db("SELECT * FROM dojos;") #queries users from DB
        all_dojos = []
        if results:
            for row in results: 
                all_dojos.append(cls(row))
            return all_dojos


    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;" # Sanitize what users put in to prevent unwanted data
        results = connectToMySQL("dojos_and_ninjas_db").query_db(query, data) #assign var bc when query it returns a lists from db
        if results:
            return cls(results[0])

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s ;"
        results = connectToMySQL("dojos_and_ninjas_db").query_db(query, data)
        if len(results) == 0:
            return "No Ninjas Found"
        dojo = cls(results[0])
        if results:
            for row in results:
                ninja_data = {
                    "id": row["ninjas.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"],
                    "dojo_id": row["dojo_id"]
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo