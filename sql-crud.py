#4. The laast file to be created to do the CRUD functionality.
#Building class-based models to Create and Read data on your Postgres Database,
#Allows us to  define custom tables to add and retrieve records using the ORM
#Extend the ORM declarative_base to generate new tables and records
#No need to import float or foreign key
#1. Here we shall create and update
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#2. executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

#3.We are going to create a table to celebrate the all time programers
#Below is a table schema of our data or how our table will look like...after we can start adding new records on our table,
# for each new record we add, we'll assign it to a variable using the programmers name
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True) #So that they increment by 1 for every added class.
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

#These steps are inherited from the previous direct.
# Instead of connecting to the database directly, we  will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db) #To connect to database we need to call session and open an actual session
#Opens an actual session by calling the Session() subclass defined above
session = Session()

#Creating the database using declarative base subclass
base.metadata.create_all(db)

#4.Creating records on our Programmer table
#Add each instance of our programmers to our session.
ada_Lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality ="British",
    famous_for = "First Programmer"

)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality ="British",
    famous_for = "Modern computing"
)

grace_hopper= Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality ="American",
    famous_for = "COBOL language"
)

margaret_hamiltion= Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality ="American",
    famous_for = "Apollo 11"
)

bill_gates= Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality ="American",
    famous_for = "Microsoft"
)

tim_berners_lee= Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality ="British",
    famous_for = "World Wide Web"
)


allan_zizinga = Programmer(
    first_name = "Allan",
    last_name = "Zizinga",
    gender = "M",
    nationality ="Ugandan",
    famous_for = "Football"
)

#5.
#Add each instance of our programmers to our session
#session.add(ada_Lovelace)
#Before commiting the next records, we add  other programers
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamiltion)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(allan_zizinga)

#6 Then commit the changes made
#commit our session to the database
#session.commit()

#8 Updating records from the database
#Use an Id to identify which record you want to update.

#Inorder to update or delete a record, we must first identify which record needs to be, to do data retrieval

# programmer = session.query(Programmer).filter_by(id=1).first() #You must add a ".first() at the end to avaiod using a for loop"
# ...use the id to find a single record
# programmer.famous_for = "World president"

#9. Then need to commit the update.
#commit our session to the database, this commits the update to the database
#session.commit()

#10. 

#Updating multiple records...we use a new variable "people" instead since we already used programmers.

#So this for loop basically means that for person in persons, if the person.gender is equal to
#"F" then change the string to "Female" and so on.

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit() # 11. The commit happens within the loop itself


#12. 

#Deleting a single record...we prompt the user to make a response using the name of the programmer with the input
# Then query the Programmer object with the first n last name
#Then use an if statement

# fname = input("Enter a first name:")
# lname = input("Enter a last name:")

#13.Then querry the programmer table below
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

#14. We use this defensive programing to ensure that its the right programmer found.

# # Defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     comfirmation = input("Are you sure you want to delete this record? (y/n)") #We need to ensure that the user wants to delete the record permanently.
#     if comfirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit() #Then also commit the change
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#         print("No records found")

#15. last part

#Deleting multiple records
#This should be done when only deleting all records and should be aavoided as you lose everything
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

#7.
#Query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id, 
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | " 
    )