#!/usr/bin/env python

import sys, os
import pycurl, json  
  
STREAM_URL = "http://stream.twitter.com/1/statuses/filter.json?locations=-122.75,36.8,-121.75,37.8"
  
USER = os.environ["GUSER"]
PASS = os.environ["GPASS"]

class Client:  
  def __init__(self):  
    self.buffer = ""  
    self.count = 0
    self.conn = pycurl.Curl()  
    self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))  
    self.conn.setopt(pycurl.URL, STREAM_URL)  
    self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)  
    self.conn.perform()  
  
  def on_receive(self, data):  
    self.buffer += data  
    if data.endswith("\r\n") and self.buffer.strip():  
      content = json.loads(self.buffer)  
      self.buffer = ""  
      print content
      self.count = self.count + 1
      if self.count > 0:
          sys.exit(0)
  
def main():
    print """Content-type: text/json

"""
    client = Client()  
    sys.exit(0)

if __name__ == '__main__':
    main()
