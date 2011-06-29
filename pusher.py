#!/usr/bin/env python

import MySQLdb
import os

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
    c.execute("""SELECT MAX(id) AS id FROM tweets""")
    theid = c.fetchone()[0]
    theid -= 100

    c.execute("""SELECT tweet FROM tweets WHERE id >= %s LIMIT 100""", (theid,))
    print """Content-type: text/json

"""
    print '[' + ', '.join(c.fetchone()[0].strip() for i in range(100)) + ']'
    
if __name__ == '__main__':
    main()
