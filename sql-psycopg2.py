import psycopg2

#Connect to "Chinook" database
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database....A cursor object is another way of saying a "set" or 'list', similar to an 'array' in javascript.
cursor = connection.cursor()

# Querry 1 - select all records from the "Artist" table.....important that you wrap everything in single quotes.
#cursor.execute('SELECT * FROM "Artist"')
#

#Querry 2- Select only the "Name" column from the "Artist " table
#cursor.execute('SELECT "Name" FROM "Artist"')


#Querry 3 - Select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"]) #We use a python string placeholer "%s" an define the desired string in a list

#Querry 4 - select only by "ArtistId" #51 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" =%s', [51])

#Querry 5 - select only albums with "ArtistId" #51 on the "Album" table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

#Querry 6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Queen"])


#fetch the results(multiple)....Here we fetch the results
#results = cursor.fetchall()

#fetch the result (single)
results = cursor.fetchone()

#close the connection.....Here we close the ddatabase
connection.close()

#print results
for result in results:
    print(result)




