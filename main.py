import time

from initialize import initialize
from db.sqlQuerry import *

def main():
    initialize()
    bestArtist()
    top5Songs()

start_time = time.time()
main()
print("--- Finished in %.6f seconds ---" % (time.time() - start_time))
