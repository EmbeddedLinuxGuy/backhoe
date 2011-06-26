#!/usr/bin/env python

import MySQLdb
import os

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
#    c.execute("""SELECT MAX(id) AS id FROM tweet""")
    c.execute("""SELECT tweet FROM tweet LIMIT 10""")
    print """Content-type: text/json

"""
    print '[' + ', '.join(c.fetchone()[0].strip() for i in range(10)) + ']'
    
if __name__ == '__main__':
    main()
