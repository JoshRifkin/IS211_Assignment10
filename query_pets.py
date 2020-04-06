# Assignment 10
# Query Pets
# By: Joshua Rifkin

import sqlite3 as sql


def queryDB(db, personID):
    db.execute("SELECT * FROM person WHERE id = :id", {"id": personID})
    records = db.fetchone()

    outputLive = "{0} {1} owns {2}, a {3}, that is {4} years old."
    outputDead = "{0} {1} owned {2}, a {3}, that was {4} years old."

    if records is None:
        print("There is no one in the database with that ID number.\n")
    else:
        print("{} {} is {} years old".format(records[1], records[2], records[3]))
        db.execute("""
        SELECT prs.first_name, prs.last_name, pt.name, pt.breed, pt.age, pt.dead
        FROM person prs, pet pt, person_pet pp 
        WHERE prs.id = :persID
        AND pp.person_id == prs.id
        AND  pt.id == pp.pet_id""", {"persID": personID})
        petRecords = db.fetchall()

        for pet in petRecords:
            if pet[5] == 1:
                print(outputDead.format(pet[0], pet[1], pet[2], pet[3], pet[4]))
            else:
                print(outputLive.format(pet[0], pet[1], pet[2], pet[3], pet[4]))

        print("")


def main():
    conn = sql.connect("pets.db")
    db = conn.cursor()
    while True:
        query = input("Please enter the ID of the person whom you would like to query: ")
        if query == "-1":
            print("Closing Program.")
            break
        else:
            queryDB(db, query)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
