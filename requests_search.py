import json
import vk

cred = json.load(open('token.json'))
token = cred['access_token']

session = vk.Session()
api = vk.API(session)
res = api.users.search(
    access_token=token,
    city=95,
    country=1,
    university=1179,
    v=5.131
)
print(res)