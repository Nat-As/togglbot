#!/bin/bash
#Togglbot Shell requester
#James Andrews <jandrews7348@floridapoly.edu>
clear

user=jandrews7348@floridapoly.edu
pass=password

#Get API Token
APIT="$(curl -s -u $user:$pass \
-X POST https://www.toggl.com/api/v8/reset_token | sed 's/"//g')"
printf "Token:$APIT\n"

#Build DATA
date="$(date --rfc-3339=seconds | sed 's/ /T/g')"
slotv1=60
hw=calculus
wid=55555

data="description":"$hw","created_with":"togglbot","start":"$date","duration":$slotv1,"wid":$wid
req='{"time_entry":{'$data'}}'

printf "$req\n"
#Send request
curl -u $APIT:api_token \
-H "Content-Type: application/json" \
-d $req \
-X POST https://www.toggl.com/api/v8/time_entries
