import json
import time

import vk


TOKEN = json.load(open('token.json', encoding='utf-8'))['access_token']


def search(age, sex=0):
    session = vk.Session()
    api = vk.API(session)
    res = api.users.search(
        access_token=TOKEN,
        count=1000,
        age_from=age[0],
        age_to=age[1],
        sex=sex,
        # city=95,    # 95 - Нижний Новгород, 1 - Москва
        # country=1,
        university=1179,  # 1179 - НИУ ВШЭ НН
        v=5.131
    )

    data = json.load(open('users.json', 'r', encoding='utf-8'))
    data['count'] += res['count']
    data['items'].extend(res['items'])
    json.dump(
        data,
        open('users.json', 'w', encoding='utf-8'),
        indent=2,
        ensure_ascii=False
    )

    print(f'{age=} {sex=}')


def search_process():
    # n = 17304    # НИУ ВШЭ НН  # todo НИУ ВШЭ НН ФиПЛ, НИУ ВШЭ (Москва), НИУ ВШЭ Москва ФиКЛ
    ages = (
        (0, 19),    # 782
        (20, 21),   # 997
        (22, 22),   # 527
        (23, 23),   # 542
        (24, 24),   # 498
        (25, 25),   # 590
        (26, 26),   # 627
        (27, 27),   # 664
        (28, 28),   # 752
        (29, 29),   # 784
        (30, 30),   # 821
        (31, 31),   # 805
        (32, 32),   # 781
        (33, 33),   # 746
        (34, 34),   # 756
        (35, 35),   # 606
        (36, 36),   # 580
        (37, 38),   # 988
        (39, 41),   # 935
        (42, 50),   # 947
        (51, 118),  # 464
        (119, 119), # 2130: sex 1 - 1013, sex 2 - 1114
    )

    data = {'count': 0, 'items': []}
    json.dump(
        data,
        open('users.json', 'w', encoding='utf-8'),
        indent=2,
        ensure_ascii=False
    )

    for age in ages:
        time.sleep(2)
        if age == (119, 119):
            search(age, sex=1)
            search(age, sex=2)
        else:
            search(age)


if __name__ == '__main__':
    search_process()
