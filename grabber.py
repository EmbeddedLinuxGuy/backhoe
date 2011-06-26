#!/usr/bin/env python

import sys, os
import pycurl, json  
import MySQLdb

STREAM_URL = "http://stream.twitter.com/1/statuses/filter.json?locations=-122.75,36.8,-121.75,37.8"
  
USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

class Client:  
  def __init__(self):  
    self.buffer = ""  
    self.count = 0
    self.db = MySQLdb.connect(host="localhost", user=USER,
                  passwd=PASS,db="firebrowse")  
    self.c = self.db.cursor()

    self.conn = pycurl.Curl()  
    self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))  
    self.conn.setopt(pycurl.URL, STREAM_URL)  
    self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)  

    self.conn.perform()  
    # ? not reached ?

  def on_receive(self, data):  
    self.buffer += data  
    if data.endswith("\r\n") and self.buffer.strip():
      self.c.execute("""INSERT INTO tweet (tweet) VALUES (%s)""", (self.buffer,))
#      content = json.loads(self.buffer)  
      self.buffer = ""  
      self.count = self.count + 1
      if self.count % 100 == 0:
          print self.count
#      if self.count > 0:
#          sys.exit(0)
  
def main():
    client = Client()  
    # ? not reached ?
    sys.exit(0)

if __name__ == '__main__':
    main()
