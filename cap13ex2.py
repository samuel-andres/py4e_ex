# Exercise 13.2: Write a program that will prompt to enter in a url, read the JSON data from that URL using
# urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below.
# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

# http://py4e-data.dr-chuck.net/comments_42.json

from turtle import showturtle
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    surl = input('url> ')
    if len(surl) < 1: break

    urlhandler = urllib.request.urlopen(surl, context=ctx)
    dcdurlh = urlhandler.read().decode()

    try:
        jsondata = json.loads(dcdurlh)
    except:
        print('not json data')
        continue

    indented_representation = json.dumps(jsondata, indent=4)
    print(indented_representation)
    ind = 0
    locounts = list()
    for each_comment in jsondata['comments']:
        locounts.append(jsondata['comments'][ind]['count'])
        ind = ind + 1
    
    print('debug list of counts:',locounts)
    print('sum of counts', sum(locounts))
    