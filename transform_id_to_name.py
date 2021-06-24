from collections import Counter, OrderedDict
import json
from pprint import pprint

data = json.load(open('career.json', encoding='utf-8'))

group_ids = [
    str(place.get('group_id')) for place in
    sum([lst for lst in data.values()], [])

]

stat = Counter(group_ids)
pprint(stat)

json.dump(
    stat,
    open('career_stat.json', 'w', encoding='utf-8'),
    indent=2,
    ensure_ascii=False
)
