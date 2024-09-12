

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


