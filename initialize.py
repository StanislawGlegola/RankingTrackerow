from db.databaseHandler import *

def setDB():
    createDBTracks()
    createDBTriplets()
    checkIfDatabaseIsEmptyAndFillIt()

def initialize():
    setDB()
