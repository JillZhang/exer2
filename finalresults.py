import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

# Connect to the database
try:
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
    print "Cannot connec to tcount, please make you create the database."
cur = conn.cursor()
if len(sys.argv) > 1:
    cur.execute("SELECT word, count from tweetwordcount where word = %s",(sys.argv[1],))
    records = cur.fetchall()
    if cur.rowcount == 0:
	print "The enter word is not in the database"
    else:
        print records[0]
else:
    cur.execute("SELECT word, count from tweetwordcount order by word")
    if cur.rowcount == 0:
        print "You haven't collect any data"
    else:

        records = cur.fetchall()
        for rec in records:
            print rec
