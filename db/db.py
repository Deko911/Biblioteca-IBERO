import sqlite3

connection = sqlite3.connect("./db/db.sqlite")
connection.autocommit = True
cursor = connection.cursor()
