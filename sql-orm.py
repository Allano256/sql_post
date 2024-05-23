#3. Third file to be opened

#Using ORM and class-based models, we've reached the most Pythonic mehod and highest level of abstraction.
#Introduction to ORM(Object Relational Mapping), AN OBJECT-RATIONAL MAPPER, Bridges the gap between Python objects and Postgres tables
#Querries and manipulates a database using python, instead of raw SQL commands.
#This alows us to manipulate ata from our database using objects
#The most popular ORM libraries when working with python are the Django ORM, and SQLAlchemy which both work well with postgres.
#Advantages of SQLAlchemy include having cleaner code, the logic is simple and your code is more secure than using raw SQL commands

#1.First step is install SQLAlchemy in terminal pip3 install SQLAlchemy(current version)
#2. CREATE FILE "sql-orm.py"
#But here we can ignore table and metadata while importing because we are not going to be creating tables but python classes.
#3. Make the imports below.
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker #instead of making a connection to the database directly, we'll be asking for a session.

#4. executing the instructions from the "chinook" database 
db = create_engine("postgresql:///chinook")#This tells the application that we are using postgresql, on a local host and using the chinook databse
base = declarative_base()#The 'base' class will essentially grab the metadata that is produced by our database,table schema, and creates a subclass to map everything back to us 
#here within the 'base' variable.

#7.Only build a normal Python object, that subclasses "base"
#Make sure these are added before the Session is created, but after the base is declared.
#Create a class/based model for the "Artist" table
#Define classes with uppercase and no underscores

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)

#Create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId")) #The "Artist.ArtistId" pooints to the ArtisId in the Artist class ArtisId column.

#Create a class-based model for the "track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key = True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key = False)
    GenreId = Column(Integer, primary_key = False)
    Composer = Column(String) #Doesnt use a foreign key
    Milliseconds = Column(Integer, primary_key = False)
    Bytes = Column(Integer, primary_key = False)
    UnitPrice = Column(Float)





#5. Instead of connecting to the database directly, we  will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)
#To connect to database we need to call session and open an actual session
#Opens an actual session by calling the Session() subclass defined above
Session = sessionmaker(db) 
session = Session()

#6.Creating the database using declarative_base subclass...and generate all the metadata
base.metadata.create_all(db)

#8. We the start to querry the database
# Querry 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ") #We use the python separator, to separate the two results

#Querry 2 - Select only the "Name" column from the "Artist " table
#artists = session.query(Artist)
#for artist in artists:
   # print(artist.Name) 


#Querry 3 - Select only "Queen" from the "Artist" table.....the new variable will be singular "artist" and also use the .filter_by() and also since only 
#one item will be returned we use the .first() at the end.
#artist = session.query(Artist).filter_by(Name="Queen").first()
#print(artist.ArtistId, artist.Name, sep= " | ") 

# Query 4 - select only by 'ArtistId' #51 from the "Artist" table
#artist = session.query(Artist).filter_by(ArtistId=51).first()
#print(artist.ArtistId, artist.Name, sep= " | ")

 # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table....Here we set a new variable of albums since there are multiple albums
#albums = session.query(Album).filter_by(ArtistId=51)
#for album in albums:
    #print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

 # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table.....We must create a new variable tracks
tracks = session.query(Track).filter_by(Composer = "Queen")
for track in tracks:
    print(
         track.TrackId,
         track.Name,
         track.AlbumId,
         track.MediaTypeId, 
         track.GenreId,
         track.Milliseconds, 
         track.Bytes, 
         track.UnitPrice,
         sep=" | ")