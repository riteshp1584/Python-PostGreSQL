import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="xxxxxxxxxxxxxxx", # check Passwords file for password
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL")

conn.close()
