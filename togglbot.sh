#!/bin/bash
#Togglbot Shell requester
#James Andrews <jandrews7348@floridapoly.edu>
clear

user=jandrews7348@floridapoly.edu
pass=password
wid=3164178

#Get API Token
APIT="$(curl -s -u $user:$pass \
-X POST https://www.toggl.com/api/v8/reset_token | sed 's/"//g')"
printf "Token:$APIT\n"

#Get WID (Workspace ID)
curl -s -u $APIT:api_token -X GET https://www.toggl.com/api/v8/me | ./jq -r '.default_wid'

#Build DATA
python="$(./togglbot.py)"
date="$(date --rfc-3339=seconds | sed 's/ /T/g')"
slotv1="$(./togglbot.py)"
hw="$(./togglthings.py)"

printf "$hw "
printf "$python"
printf " Minutes\n"

#Send request
printf "\nSending...\n"
curl -s -u $APIT:api_token \
	-H "Content-Type: application/json" \
	-d '{"time_entry":{"description":"'$hw'","created_with":"togglbot","start":"'$date'","duration":"'$slotv1'","wid":'$wid'}}' \
	-X POST https://www.toggl.com/api/v8/time_entries
printf "\n"
