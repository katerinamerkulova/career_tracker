import json
import requests

cred = json.load(open('credentials.json'))

print(requests.get(
    'https://api.linkedin.com/v2/jobs',
    # params = {
    #     # Any API params go here
    # },
    headers={
        'Authorization': 'Bearer ' + cred['access_token'],
    },
).json()
      )
