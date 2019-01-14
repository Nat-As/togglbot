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

ustring = "email@floridapoly.edu:PASSWORD"
username = "email@floridapoly.edu"
password ="Password123"

# SEED
seed = randint(11111,99999)
slotv1 = randint(20,59)
slotv2 = randint(20,59)
slotv3 = randint(20,59)
slotv4 = randint(20,59)
slotv5 = randint(20,59)
slotv6 = randint(20,59)
slotv7 = randint(20,59)
slotv8 = randint(20,59)

date = datetime.datetime.now()
#Add more activities to add more entropy and make it more interesting! |

hw = ["Calculus", "Break", "Study", "Physics", "LAB", "Misc.", "Robotics", "Programming", "Study group", "Project", "C&M"]

#LOG DATA (before sending)

print random.choice(hw)
#print slotv2, "Minutes", random.choice(hw)
#print slotv3, "Minutes", random.choice(hw)
#print slotv4, "Minutes", random.choice(hw)
#print slotv5, "Minutes", random.choice(hw)
#print slotv6, "Minutes", random.choice(hw)
#print slotv7, "Minutes", random.choice(hw)
#print slotv8, "Minutes", random.choice(hw)

v1 = slotv1, "Minutes", random.choice(hw)
v2 = slotv2, "Minutes", random.choice(hw)
v3 = slotv3, "Minutes", random.choice(hw)
v4 = slotv4, "Minutes", random.choice(hw)
v5 = slotv5, "Minutes", random.choice(hw)
v6 = slotv6, "Minutes", random.choice(hw)
v7 = slotv7, "Minutes", random.choice(hw)
v8 = slotv8, "Minutes", random.choice(hw)
