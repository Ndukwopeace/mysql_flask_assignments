from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['Last_name']
        self.email = data['Email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

# to add a user ========================
    @classmethod 
    def add_user(cls,data):
        query = "INSERT INTO users(first_name,Last_name,Email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,now(),now());"
        return connectToMySQL('users_schema').query_db(query,data)
        

# to show all users
    @classmethod 
    def show_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
    
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users