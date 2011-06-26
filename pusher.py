#!/usr/bin/env python

import MySQLdb
import os

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
    c.execute("""SELECT tweet from tweet LIMIT 100""")
    v = c.fetchone()
    print """Content-type: text/json

"""
    print v
    
if __name__ == '__main__':
    main()
