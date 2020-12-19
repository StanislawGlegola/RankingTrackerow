import sqlite3

tripletsSampleTxt=open("resources/triplets_sample_20p.txt")
tripletsSampleSQLInsertQuery = """INSERT INTO triplets_sample (userID, trackID, listenDate) VALUES (?,?,?) """

uniqueTracksTxt=open("resources/unique_tracks.txt")
uniqueTracksSQLInsertQuery = """INSERT INTO unique_tracks (authorID, trackID, artist, title, duration) VALUES (?,?,?,?,?) """

conn = sqlite3.connect("db/tracker.db")
c=conn.cursor()

def checkIfDatabaseIsEmptyAndFillIt():
    r=c.execute("""SELECT * from triplets_sample""").fetchall()
    p=c.execute("""SELECT * from unique_tracks""").fetchall()

    if len(r) == 0 or len(p) == 0:
        print("Updating database...")
        fillDB(tripletsSampleTxt, tripletsSampleSQLInsertQuery)
        fillDB(uniqueTracksTxt, uniqueTracksSQLInsertQuery)
    else:
        print("Database loaded\n")

def createDBTriplets():
    c.execute("""CREATE TABLE IF NOT EXISTS triplets_sample (
            userID TEXT,
            trackID TEXT,
            listenDate TEXT
            )""")

def createDBTracks():
    c.execute("""CREATE TABLE IF NOT EXISTS unique_tracks (
            authorID TEXT,
            trackID TEXT,
            artist TEXT,
            title TEXT,
            duration INTEGER 
            )""")

def fillDB(textFile,mySqlInsertQuery):
    for line in textFile:
        line = line.replace("\n", "")
        data = line.split(";")
        c.execute(mySqlInsertQuery, data)
        conn.commit()
    #conn.close()

#createDBTracks()
#createDBTriplets()