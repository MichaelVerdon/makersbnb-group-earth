"""
Test to see if space creation works
POST /create-space
"""
def test_create_space(db_connection, web_client):
    db_connection.seed("seeds/makersbnb.sql")

    response = web_client.post("/create-space", data={
        'name':'Castle', 
        'description':'A lovely castle.', 
        'price_per_night':500, 
        'availability_start':'2024-12-25', 
        'availability_end':'2024-12-27', 
        'user_id':2
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Space added successfully"

    response = web_client.get("/all-spaces")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Space(1, Beach House, A beautiful beach house with ocean view., 150, 2024-09-15, 2024-09-30, 3)",
        "Space(2, Tree House, A house my dad build in my backyard, 125, 2024-10-11, 2024-11-30, 1)",
        "Space(3, Mountain Cabin, A cozy cabin in the mountains., 120, 2024-10-01, 2024-10-15, 4)",
        "Space(4, Castle, A lovely castle., 500, 2024-12-25, 2024-12-27, 2)"
    
    ])

"""
Test to see if we can list all spaces
GET /all-space
"""

def test_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/makersbnb.sql")
    response = web_client.get("/all-spaces")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Space(1, Beach House, A beautiful beach house with ocean view., 150, 2024-09-15, 2024-09-30, 3)",
                    "Space(2, Tree House, A house my dad build in my backyard, 125, 2024-10-11, 2024-11-30, 1)",
                    "Space(3, Mountain Cabin, A cozy cabin in the mountains., 120, 2024-10-01, 2024-10-15, 4)"
    
    ])


