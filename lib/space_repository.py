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
        rows = self.connection.execute('INSERT INTO spaces (name, description, price_per_night, availability_start, availability_end, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [space.name, space.description, space.price_per_night, space.availability_start, space.availability_end, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def get_by_id(self, id):
        row = self.connection.execute(f"SELECT * FROM spaces WHERE id = {id}")[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"],\
                        str(row["availability_start"]), str(row["availability_end"]), row["user_id"])

    def get_by_user_id(self, user_id):
        """Returns list of spaces for given user_id"""
        rows = self.connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price_per_night"],\
                        str(row["availability_start"]), str(row["availability_end"]), row["user_id"])
            spaces.append(item)
        return spaces
    

    #this will update each detail of the space given the space's name
    
    def update_name(self, space_id, new_name):
        self.connection.execute("UPDATE spaces SET name=%s  WHERE id= %s", [new_name, space_id])


    def update_description(self, space_id, new_description):
        self.connection.execute("UPDATE spaces SET description=%s  WHERE id= %s", [new_description, space_id])



    def update_price_per_night(self, space_id, new_price_per_night):
        self.connection.execute("UPDATE spaces SET price_per_night=%s  WHERE id= %s", [new_price_per_night, space_id])

    def update_availability_start(self, space_id, new_availability_start):
        self.connection.execute("UPDATE spaces SET availability_start=%s  WHERE id= %s", [new_availability_start, space_id])


    def update_availability_end(self, space_id, new_availability_end):
        self.connection.execute("UPDATE spaces SET availability_end=%s  WHERE id= %s", [new_availability_end, space_id])

    def delete(self, space_id):
        self.connection.execute('DELETE FROM spaces WHERE id = %s', [space_id])






