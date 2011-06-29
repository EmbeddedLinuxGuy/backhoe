#!/usr/bin/env python

import httplib2
import json
import os
import MySQLdb
import sys

USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

def dumptweet(to_id):
    url = "http://api.twitter.com/1/statuses/show/"+str(to_id)+".json"
    try:
        http = httplib2.Http()
        r, c = http.request(url)
    except httplib2.ServerNotFoundError:
        print "Problem with url [" + url + "]"
        sys.exit(1)
        
    db2 = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    insert = db2.cursor()

    content = json.loads(c)
    try:
        if content["geo"]:
            insert.execute("""UPDATE pairs SET to_lat=%s,to_long=%s WHERE in_reply_to_status_id=%s""",
                           (content["geo"]["coordinates"][0], content["geo"]["coordinates"][1], to_id))
        else:
            insert.execute("""UPDATE pairs SET to_lat=%s,to_long=%s WHERE in_reply_to_status_id=%s""",
                           (666, 666, to_id))
    except KeyError:
        print json.dumps(content, indent=4, sort_keys=True)
        print "Problem with to_id " + str(to_id)
        insert.execute("""UPDATE pairs SET to_lat=%s,to_long=%s WHERE in_reply_to_status_id=%s""",
                       (666, 666, to_id))

def main():
    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    cur = db.cursor()

    cur.execute("""SELECT id,in_reply_to_status_id FROM pairs WHERE to_lat IS NULL LIMIT 20""")
    for i in range(20):
        [from_id, to_id] = cur.fetchone()
        dumptweet(to_id)

if __name__ == '__main__':
    main()
