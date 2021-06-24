import json
import time

import vk

TOKEN = json.load(open('token.json', encoding='utf-8'))['access_token']


def iterate():
    users = json.load(open('users.json', 'r', encoding='utf-8'))
    session = vk.Session()
    api = vk.API(session)

    for i in range(0, len(users['items']), 1000):
        time.sleep(2)
        subset = users['items'][i:i + 1000]
        ids = [person['id'] for person in subset]
        info = api.users.get(
            access_token=TOKEN,
            user_ids=ids,
            fields='career',
            v=5.131
        )

        career = {
            person['id']: person['career']
            for person in info
            if person.get('career')
        }

        data = json.load(open('career.json', 'r', encoding='utf-8'))
        data |= career
        json.dump(
            data,
            open('career.json', 'w', encoding='utf-8'),
            indent=2,
            ensure_ascii=False
        )


if __name__ == '__main__':
    iterate()
