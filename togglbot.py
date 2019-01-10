#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import datetime
import http.client
import sys
import re
import random

from urlparse import urlparse
from six.moves.urllib.parse import urlparse
from random import randint
from HTMLParser import HTMLParser
if ((3, 0) <= sys.version_info <= (3, 9)):
    from urllib.parse import urlparse
elif ((2, 0) <= sys.version_info <= (2, 9)):
    from urlparse import urlparse

# SEED
seed = (randint(10,60))
slotv1 = (randint(10,60))
slotv2 = (randint(10,60))
slotv3 = (randint(10,60))
slotv4 = (randint(10,60))
slotv5 = (randint(10,60))

slot1 = abs(slotv1)
slot2 = abs(slotv2)
slot3 = abs(slotv3)
slot4 = abs(slotv4)
slot5 = abs(slotv5)

#params = urlparse.urlencode({'@number': 12524, '@type': 'issue','@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

# SETUP
conn = http.client.HTTPSConnection("www.toggl.com")
conn.request("GET","/")
r1 = conn.getresponse()
print(r1.status,r1.reason) #200 OK

data1 = r1.read()#content
conn.request("GET","/")
r1 = conn.getresponse()
#while not r1.closed:
print(len(r1.read(200)))#200 bytes
print("Bytes recieved")

#LOGIN
#https://togglstats.toggl.com/in.php?site_id=100991496&type=ping&jsuid=3406503203&mime=js&x=0.5637338976052283
loginparams = 
loginheaders = 
conn.request("POST", "", loginparams, loginheaders)
response = conn.getresponse()
print("Login status:\n")
print(response.status, response.reason) #Login Status
#print(response.read())

#Logout
now = datetime.datetime.now()#note the time
HTTPConnection.close('www.toggl.com')
print("Logout")
print(now.month,now.day,now.year)
