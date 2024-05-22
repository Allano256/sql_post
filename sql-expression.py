#Import these classes from the sqlalchemy
#from sqlalchemy import (
  #  create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
#)

# LINK OUR PYTHON FILE TO OUR CHINOOK DATABASE,THATS WHERE THE CREATE_ENGINE COMES INTO PLACE Executing the instructions from our localhost "chinook" "db to represent database"
#db = create_engine("postgresql:///chinook") #The three slashes mean that our database is hosted locally.

#meta = MetaData(db) #The MetaDATA CLASS WILL COMNTAIN A COLLECTION OF OUR TABLE OBJECTS, AND ASSOCIATED DATA WITHIN THOS OBJECTS

# create variable for "Artist" table
#artist_table = Table(
   # "Artist", meta,
    #Column("ArtistId", Integer, primary_key = True),
    #Column("Name", String)
#)

# Create variable for "Album" table
#artist_table = Table(
   # "Album", meta,
    #Column("AlbumId", Integer, primary_key = True),
   # Column("Title", String),
   # Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId")) #With the foreign key we need to tell it which table and key to point to so in this case its the artist_table.ArtistId
#)

# Create variable for "Track" table

#track_table = Table(
    #"track",meta,
   # Column("TrackId", Integer, primary_key = True),
    #Column("Name", String),
   # Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    #Column("MediaTypeId", Integer, primary_key=False),
   # Column("GenreId", Integer, primary_key=False),
   # Column("Composer", String),
   # Column("Milliseconds", Integer),
    #Column("Bytes", Integer),
   # Column("UnitPrice", Float)
#)


# MAKING THE CONNECTION TO THE DATABASE....the "with statement saves our connection to the database into a variable called connection"
#with db.connect() as connection:

    # Querry 1 - select all records from the "Artist" table.....important that you wrap everything in single quotes.
    #select_query = artist_table.select()

    #Querry 2- Select only the "Name" column from the "Artist " table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name]) # If we want to grab results from a single column, we need to wrap the column selection inside of a list. Also using the dot-notation, we need to use ".c" in our selection, which will idenbtify a specific column header on the table.

    #Querry 3 - Select only "Queen" from the "Artist" table
   # select_query = artist_table.select().with_only_columns([artist_table.c.Name == "Queen"])
  


    #results = connection.execute(select_query) #We store the outcome in results variable
    #for result in results:
       # print(result)









#Import these classes from the sqlalchemy
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)

