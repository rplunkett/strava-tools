#!/usr/bin/env python3
import requests
import simplejson as json
import sys

input_file = sys.argv[1]

with open(input_file) as fin:
    all_activities = fin.read().splitlines()

headers = {"content-type": "application/json"}
update_data = {"gear_id": "b2559573"}

for activity in all_activities:
    put_url = 'https://www.strava.com/api/v3/activities/%s?access_token=access_token' % (activity)
    req = requests.put(put_url, data=json.dumps(update_data), headers=headers)
    print('Response %s for %s' % (req.status_code, activity))
