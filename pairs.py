#!/usr/bin/env python

import MySQLdb
import os
import json

def main():
    USER = os.environ["GUSER"]
    PASS = os.environ["GPASS"]

    db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    c = db.cursor()
    c.execute("""SELECT MAX(id) AS id FROM tweet""")
    theid = c.fetchone()[0]

    c.execute("""SELECT tweet FROM tweet WHERE id <= %s ORDER BY ID""", (theid,))
    print """Content-type: text/json

"""
    for i in range(293):
      content = json.loads(c.fetchone()[0].strip())
      if content["id"] and content["in_reply_to_status_id"] and content["geo"]:
          insert = db.cursor()
          insert.execute("""INSERT INTO pairs (id,in_reply_to_status_id,from_lat,from_long)"""
                         """VALUES (%s,%s,%s,%s)""",
                         (content["id"], content["in_reply_to_status_id"],
                          content["geo"]["coordinates"][0], content["geo"]["coordinates"][1]))

#      print json.dumps(content, indent=4, sort_keys=True)
#      print content["id_str"]
#      print content["id"]
#      print content["in_reply_to_screen_name"]
#      print content["in_reply_to_user_id"]
#      print content["in_reply_to_user_id_str"]
#      print content["in_reply_to_status_id"]
#      print content["in_reply_to_status_id_str"]

if __name__ == '__main__':
    main()
