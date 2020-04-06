# Assignment 10
# Load Pets
# By: Joshua Rifkin


import sqlite3 as sql


def createDB(db):
    # Delete tables if they already exist, prepping for creation
    db.execute("DROP TABLE IF EXISTS person;")
    db.execute("DROP TABLE IF EXISTS pet;")
    db.execute("DROP TABLE IF EXISTS person_pet;")

    # Create Tables
    db.execute("CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);")
    db.execute("CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);")
    db.execute("CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER);")

    # Populate person table
    db.execute("INSERT INTO person VALUES(1, 'James', 'Smith', 41);")
    db.execute("INSERT INTO person VALUES(2, 'Diana', 'Greene', 23);")
    db.execute("INSERT INTO person VALUES(3, 'Sara', 'White', 27);")
    db.execute("INSERT INTO person VALUES(4, 'William', 'Gibson', 23);")

    # populate pet table
    db.execute("INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1);")
    db.execute("INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0);")
    db.execute("INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0);")
    db.execute("INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0);")
    db.execute("INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0);")
    db.execute("INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1);")

    # populate person_pet table to connect pets to owners with JOIN statements
    db.execute("INSERT INTO person_pet VALUES(1, 1);")
    db.execute("INSERT INTO person_pet VALUES(1, 2);")
    db.execute("INSERT INTO person_pet VALUES(2, 3);")
    db.execute("INSERT INTO person_pet VALUES(2, 4);")
    db.execute("INSERT INTO person_pet VALUES(3, 5);")
    db.execute("INSERT INTO person_pet VALUES(4, 6);")


def main():
    conn = sql.connect("pets.db")
    db = conn.cursor()
    createDB(db)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
