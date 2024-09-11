from lib.space import Space

class SpaceRepository():

    def __init__(self, connection):
        self.connection = connection 

#this will return all the spaces of the database
    def all(self):
        rows = self.connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price_per_night"],\
                        str(row["availability_start"]), str(row["availability_end"]), row["user_id"])
            spaces.append(item)
        return spaces
        
#Function to add a space to the database
    def create(self, space):
        rows =self.connection.execute('INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [space.name, space.description, space.price_per_night, space.availability_start, space.availability_end, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def remove_space(self, name):
        self.connection.execute('DELETE FROM spaces WHERE name = %s', [name])
