# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 15:28:28 2017

@author: jill zhang
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

# Connect to the database
try:
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
except:
    print "Cannot connect to tcount database. Please make you create the database first"
cur = conn.cursor()

if len(sys.argv) != 3:
    raise ValueError('Incorrect range input. Please re-try')

cur.execute("SELECT word, count from tweetwordcount where count > %s and count < %s order by count desc",(sys.argv[1],sys.argv[2]))
if cur.rowcount == 0:
    print "Cannot find word with you specified range, please change your statement"
else:
    records = cur.fetchall()

    for rec in records:
        print "%s : %s" %rec
    
