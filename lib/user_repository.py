from lib.user import User

class UserRepository:
    def __init__(self, conection):
        self._connection = conection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        return [User(row['id'], row['email'], row['password'], row['username']) for row in rows]
    
    def create(self, email, password, username):
        self._connection.execute('INSERT INTO users (email, password, username) VALUES (%s, %s, %s)', [email, password, username]) 

    def get_by_id(self, id):
        row = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])[0]
        return User(row['id'], row['email'], row['password'], row['username'])
