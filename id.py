#!/usr/bin/env python

import httplib2
import cgi

def dumptweet(theid):
    url = "http://api.twitter.com/1/statuses/show/"+theid+".json"
    print """Content-type: text/json
""";
    try:
        http = httplib2.Http()
        r, c = http.request(url)
    except httplib2.ServerNotFoundError:
        print "Problem with url [" + url + "]"
        sys.exit(1)
    print c

def main():
    form = cgi.FieldStorage()
    dumptweet(form["tweetid"].value)

if __name__ == '__main__':
    main()
