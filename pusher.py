#!/usr/bin/env python

import MySQLdb
import os

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
    c.execute("""SELECT tweet FROM tweet LIMIT 100""")
    print """Content-type: text/json

"""
    for i in range(10):
        v = c.fetchone()
        print v[0].strip()
    
if __name__ == '__main__':
    main()
