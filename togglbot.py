#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import datetime
import http.client
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

hw = ["Calculus", "Break", "Study"]

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

#SEND DATA
conn.request("HEAD", "dataparams1, dataheaders2")#1st request
conn.request("POST", "dataparams1, dataheaders2")#1st request

#Logout
now = datetime.datetime.now()#note the time
HTTPConnection.close('www.toggl.com')
print("Logout")
print(now.month,now.day,now.year)
