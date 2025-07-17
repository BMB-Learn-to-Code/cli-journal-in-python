import sqlite3
import datetime

connection  = sqlite3.connect("data.db")


def create_db():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def close_connection():
    connection.close()

def add_items():
    new_story = input("Enter your entry for today:\n")
    new_date = datetime.datetime.now()
    with connection:
        connection.execute("INSERT INTO entries VALUES(?,?)", (new_story, new_date))

def view_items():
    entries = []
    with connection:
        entries = connection.execute("SELECT * FROM entries").fetchall()
    for entry in entries:
        print(f"{entry[1]} - {entry[0]}\n")
