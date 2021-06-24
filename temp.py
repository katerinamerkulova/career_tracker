import json
import vk


TOKEN = json.load(open('token.json', encoding='utf-8'))['access_token']


def transform(id):
    session = vk.Session()
    api = vk.API(session)
    res = api.groups.getById(
        access_token=TOKEN,
        group_id=24011636,
        v=5.131
    )
    return res['name']
