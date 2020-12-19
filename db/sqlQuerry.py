import sqlite3

conn = sqlite3.connect("db/tracker.db")
c = conn.cursor()

def bestArtist():
    print('Most popular artist')
    selectQuery =   'select artist, count(*) from triplets_sample join unique_tracks ' \
                    'ON triplets_sample.trackID = unique_tracks.trackID ' \
                    'group by artist order by count(*) DESC'
    rows = c.execute(selectQuery).fetchone()
    print(rows[0]+"\n")

def top5Songs():
    print('5 songs with highest amount of listeners')
    selectQuery = 'select title, count(*)  FROM triplets_sample JOIN unique_tracks ' \
                  'ON triplets_sample.trackID = unique_tracks.trackID  ' \
                  'group by title order by count(*) DESC'
    rows = c.execute(selectQuery).fetchmany(5)
    for row in rows:
        print("Title: " + row[0] + " with " +str(row[1]) + " listeners.")
