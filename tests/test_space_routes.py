


# """
# POST /books
# """
# def test_create_book(db_connection, web_client):
#     db_connection.seed("seeds/book_store.sql")

#     response = web_client.post("/books", data={
#         "title": "The Great Gatsby",
#         "author_name": "F. Scott Fitzgerald"
#     })

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Book added successfully"

#     response = web_client.get("/books")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "\n".join([
#         "Book(1, Invisible Cities, Italo Calvino)\n" +
#         "Book(2, The Man Who Was Thursday, GK Chesterton)\n" +
#         "Book(3, Bluets, Maggie Nelson)\n" +
#         "Book(4, No Place on Earth, Christa Wolf)\n" +
#         "Book(5, Nevada, Imogen Binnie)\n" +
#         "Book(6, The Great Gatsby, F. Scott Fitzgerald)"
#     ])