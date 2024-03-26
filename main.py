import psycopg2
from author import Author

conn = psycopg2.connect(
    dbname = "bphzurc4badokyq3ezig",
    user = "ucrksoznquj3b71nfqcv",
    password = "2YKt1zZxmkqsYgV41W3260QJNXRTn6",
    host = "bphzurc4badokyq3ezig-postgresql.services.clever-cloud.com",
    port = "50013"
)

# print(conn)

cursor = conn.cursor()
#
# print(cursor)
#
# cursor.execute("SELECT * FROM authors")
# autori = cursor.fetchall()
# print(autori)
#
cursor.execute("SELECT * FROM authors")
prvy_autor = cursor.fetchone()
print(prvy_autor)
#
# cursor.execute("SELECT * FROM authors ORDER BY author_id DESC")
# posledny_autor = cursor.fetchone()
# print(posledny_autor)


# prvy_autor = Author(prvy_autor[0], prvy_autor[1], prvy_autor[2])
#
# print("---- FIRST AUTHOR----")
# print("Author ID:   ", prvy_autor.author_id)
# print("Name:        ", prvy_autor.meno)
# print("Email:       ", prvy_autor.bio)


# author_id = prvy_autor.author_id
# meno = prvy_autor.meno
# bio = prvy_autor.bio

nejakyauthor = Author(prvy_autor[0], prvy_autor[1], prvy_autor[2])

print(nejakyauthor)

cursor.execute("SELECT * FROM books WHERE publication_year > %s AND publication_year < %s", (1900,1950))
knihy = cursor.fetchall()
print(knihy)

a=input(("zadaj zaner"))
cursor.execute("select b.title from books b inner join genres g on g.genre_id = b.genre_id where g.name = %s",(a,))
zaner = cursor.fetchall()
print(zaner)

cursor.execute("""
INSERT INTO books (title, author_id, genre_id, ISBN, publication_year, copies )
VALUES (%s, %s, %s, %s, %s, %s)
""", ("prezidnet", 4, 3, 9780747532587, 1998, 2))

conn.commit()



cursor.close()
conn.close()