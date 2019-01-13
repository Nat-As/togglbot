#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import datetime
import http.client
import urllib2
import requests
import json
import sys
import re
import os
import platform
import random

from urlparse import urlparse
from six.moves.urllib.parse import urlparse
from random import randint
from HTMLParser import HTMLParser
if ((3, 0) <= sys.version_info <= (3, 9)):
    from urllib.parse import urlparse
elif ((2, 0) <= sys.version_info <= (2, 9)):
    from urlparse import urlparse

logindata = "email@floridapoly.edu:PASSWORD"
username = "email@floridapoly.edu"
password ="Password123"

# SEED
seed = randint(10,60)
slotv1 = randint(10,59)
slotv2 = randint(10,59)
slotv3 = randint(10,59)
slotv4 = randint(10,59)
slotv5 = randint(10,59)
slotv6 = randint(10,59)
slotv7 = randint(10,59)
slotv8 = randint(10,59)

time = datetime.time() #now.time
day = datetime.day() #now.day
month = datetime.month() #now.month

hw = ["Calculus", "Break", "Study", "Physics", "LAB", "Misc.", "Robotics", "Programming", "Study group", "Project"]

#params = urlparse.urlencode({'@number': 12524, '@type': 'issue','@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

# SETUP
print"Running on:", platform.system(),platform.release()
conn = http.client.HTTPSConnection("www.toggl.com")
conn.request("GET","/")
r1 = conn.getresponse()
print "STATUS", r1.status,r1.reason #200 OK

data1 = r1.read()#content
conn.request("GET","/")
r1 = conn.getresponse()
#while not r1.closed:
print("Bytes recieved:")
print(len(r1.read(200)))#200 bytes

#LOG DATA (before sending)
print "DATA:"
print "========="
print slotv1, "Minutes", random.choice(hw)
print slotv2, "Minutes", random.choice(hw)
print slotv3, "Minutes", random.choice(hw)
print slotv4, "Minutes", random.choice(hw)
print slotv5, "Minutes", random.choice(hw)
print slotv6, "Minutes", random.choice(hw)
print slotv7, "Minutes", random.choice(hw)
print slotv8, "Minutes", random.choice(hw)

#Authenticate with API

#SEND DATA
#apitoken = 2#API secret


req = urllib2.request(www.toggl.com)
req.add_header('%s', ":", "%s" username, password)#header? curl -u
req.add_header("Content-Type", "application/json")
req.add_header('{"time_entry":{"description":"New time entry","created_with":"togglbot","start":"2019-%i-%iT%i:%i+00:%i","duration":%i, "wid":%i}}' % day, month, time, slotv1)

res = urllib2.urlopen(req)
print res.read(req)

connection = http.client.HTTPSConnection('www.toggl.com')
r = requests.get('www.toggl.com', auth=('logindata'))
print "Logging in:", r.status_code

#RETRIEVE DATA


#conn.request("HEAD", "dataparams1, dataheaders2")#1st request
#conn.request("POST", "dataparams1, dataheaders2")#1st request

#Logout
now = datetime.datetime.now()#note the time
HTTPConnection.close('www.toggl.com')
print("Logout")
print(now.month,now.day,now.year)
