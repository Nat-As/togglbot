# TogglBot
A simple http bot in python that uses the toggl API
## API Documentation
+ https://github.com/toggl/toggl_api_docs

## Summary
A python bot that automatically submits psuedo-random info into a scheduler field on toggl. (www.toggl.com)
Developed to do my homework for me.

## Installation
+ After cloning into the repository file:
1. pip install requests
2. **install jq
  - https://stedolan.github.io/jq/
  - rename it "jq"
  - place in the togglbot file**
3. chmod -R a+rwx togglbot
4. edit the shell script (Lines 6 and 7) with your toggl email and password
5. you might need to change your workspace ID (Line 8)
6. run the shell script

## Troubleshooting
+ If you can't see the changes on your toggl report, make sure your API token appears on the terminal. If it does not, your password may be incorrect.
+ Can't find my **WID** for line 8
  -Use this command and find "default_wid"
  -curl -s -u username:password -X GET https://www.toggl.com/api/v8/me
