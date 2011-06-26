#!/usr/bin/env python

import MySQLdb
import os

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
    c.execute("""SELECT MAX(id) AS id FROM tweet""")
    theid = c.fetchone()[0]
    theid -= 10

    c.execute("""SELECT tweet FROM tweet WHERE id >= %s LIMIT 10""", (theid,))
    print """Content-type: text/json

"""
    print '[' + ', '.join(c.fetchone()[0].strip() for i in range(10)) + ']'
    
if __name__ == '__main__':
    main()
