from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for use in results:
            users.append( cls(use) )
        return users
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL('users_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        return results
    
    @classmethod
    def update_one(cls, data):
        query = "UPDATE users "
        query += "SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s "
        query += "WHERE id = %(id)s;"
        results = results = connectToMySQL('users_schema').query_db(query,data)
        return results