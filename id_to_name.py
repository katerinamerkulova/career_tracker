import json
import time

import vk

TOKEN = json.load(open('token.json', encoding='utf-8'))['access_token']


def transform(ids):
    time.sleep(0.3)
    session = vk.Session()
    api = vk.API(session)
    res = api.groups.getById(
        access_token=TOKEN,
        group_ids=ids,
        v=5.131
    )
    return [company['name'] for company in res]


if __name__ == '__main__':
    careers = json.load(open('career_id.json', encoding='utf-8'))
    buffer = []
    stat = {}
    for career in careers:
        buffer.append(int(career))
        if len(buffer) == 500:
            names = transform(buffer)
            for i in range(len(names)):
                stat[names[i]] = careers[str(buffer[i])]
            buffer = []
    else:
        names = transform(buffer)
        for i in range(len(names)):
            stat[names[i]] = careers[str(buffer[i])]

    json.dump(
        stat,
        open('career_stat.json', 'w', encoding='utf-8'),
        indent=2,
        ensure_ascii=False
    )
