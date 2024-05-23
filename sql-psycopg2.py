1# 1 The first to be opened or created when connecting python to postgres

#2.Then import this into our file
import psycopg2  

#3.Connect psycopg2 to "Chinook" database using the .connect method and assign it to the variable of connection

connection = psycopg2.connect(database="chinook")

#4. build a cursor object of the database....A cursor object is another way of saying a "set" or 'list', similar to an 'array' in javascript. 
# Our object needs an instance of a cursor object, everything we iterate will become apart of this cursor as we use the for loop.

cursor = connection.cursor()

#9. Then use the the execute() method before our querries are fetched.
#Must use single quotes to wrap our querry

# Querry 1 - select all records from the "Artist" table.....important that you wrap everything in single quotes.
cursor.execute('SELECT * FROM "Artist"')

#Querry 2- Select only the "Name" column from the "Artist " table
#cursor.execute('SELECT "Name" FROM "Artist"')

#Querry 3 - Select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"]) #We use a python string placeholder "%s" and define the desired string in a list

#Querry 4 - select only by "ArtistId" #51 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" =%s', [51])

#Querry 5 - select only albums with "ArtistId" #51 on the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

#Querry 6 - select all tracks where the composer is "Queen" from the "Track" table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Queen"])


#5. We need to setup a way of retrieving the data from the database(cursor) so we setup this so as to start querrying our database.
#6. So we assign the cursor() to a variable called results.

# fetch the results(multiple)....Here we fetch the results

#results = cursor.fetchall()

#fetch the result (single)
results = cursor.fetchone()

#7. Once results are fetched we must end connection to DATABASE. Close the connection.....Here we close the ddatabase
connection.close()

#8.Because our data sits in a cursor object similar to an array so we have too loop over it and print results.

for result in results:
    print(result)




