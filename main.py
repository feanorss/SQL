import psycopg2

conn = psycopg2.connect(
    dbname = "bphzurc4badokyq3ezig",
    user = "ucrksoznquj3b71nfqcv",
    password = "2YKt1zZxmkqsYgV41W3260QJNXRTn6",
    host = "bphzurc4badokyq3ezig-postgresql.services.clever-cloud.com",
    port = "50013"
)

print(conn)

cursor = conn.cursor()

print(cursor)

cursor.execute("SELECT * FROM authors")
autori = cursor.fetchall()
print(autori)

cursor.execute("SELECT * FROM authors")
prvy_autor = cursor.fetchone()
print(prvy_autor)

cursor.execute("SELECT * FROM authors ORDER BY author_id DESC")
posledny_autor = cursor.fetchone()
print(posledny_autor)

cursor.close()
conn.close()