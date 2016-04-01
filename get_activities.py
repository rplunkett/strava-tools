#!/usr/bin/env python3
import requests
import simplejson as json

API_BASE = 'https://www.strava.com/api/v3/athlete/activities?per_page=200&access_token='
access_token = 'access_token'

req = requests.get(API_BASE + access_token)
all_activites = json.loads(req.content)

for activity in all_activites:
    print(activity['id'],',',activity['name'],',',activity['type'])
