#!/usr/bin/env python

import sys, os
import pycurl, json  
import MySQLdb

loc = "-125,25,-66,50" # continental USA
STREAM_URL = "http://stream.twitter.com/1/statuses/filter.json?locations="+loc
  
USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

class Client:  
  def __init__(self):  
    self.buffer = ""  
    self.count = 0
    self.db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    self.c = self.db.cursor()
    self.max = 1000
    self.min = 1000
    self.inserts = 0

    self.conn = pycurl.Curl()  
    self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))  
    self.conn.setopt(pycurl.URL, STREAM_URL)  
    self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)  

    self.conn.perform()
    # ? not reached ?
    print "Connection done."

  def on_receive(self, data):  
    self.buffer += data
    if data.endswith("\r\n") and self.buffer.strip():
      self.c.execute("""INSERT INTO tweet (tweet) VALUES (%s)""", (self.buffer,))
#      content = json.loads(self.buffer)  
      self.buffer = ""  
      self.inserts += 1
      if self.inserts > self.max:
          self.prune()
          self.inserts = 0

  def prune(self):
    self.c.execute("""SELECT COUNT(*) FROM tweet""")
    count = c.fetchone()[0]
    if count > self.max + self.min:
      c.execute("""DELETE FROM tweet ORDER BY cur_timestamp LIMIT %s""", (count-self.min,))

def main():
    client = Client()  
    # ? not reached ?
    print "Client finished."

if __name__ == '__main__':
    main()
