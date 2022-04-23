import os
from collections import defaultdict
import json
import inspect
from pathlib import Path
import gif_sort
import sqliteclass
import random
db = sqliteclass.sqlite3class()
basepath = Path().absolute()

gif_sort_file = os.path.join(basepath, "gif_sort.py")
with open(gif_sort_file) as file:
    pass
    # bbb_set = set(line.strip() for line in file)


taglist = dir(gif_sort)
tags = []
for item in taglist:
    if item not in ["Path", "os"]:
        if not item.startswith("_"):
            # print(item)
            tags.append(item)
            try:
                pass
            except Exception as e:
                print(e)


for tag in tags:
    atag = tag
    dictorlist = getattr(gif_sort, tag)
    if isinstance(dictorlist, list):
        # print('itsa list')
        for item in dictorlist:
            print(atag, item)
            db.tag(item, atag)
    elif isinstance(dictorlist, dict):
        # print('itsa dict ')
        newlist = dictorlist.values()
        for item in newlist:
            print(atag, item)
            db.tag(item, atag)
    elif isinstance(dictorlist, str):
        print(atag, dictorlist)
        db.tag(item, atag)

    else:
        print(type(dictorlist))
    # elif isinstance(dictorlist, list):
    # pass


print("-----------------------------")

d = defaultdict(list)
d_json_file = os.path.join(basepath, "gif_tagged.json")
if not os.path.exists(d_json_file):
    with open(d_json_file, "w") as f:
        pass

else:
    with open(d_json_file) as f:
        d_str = json.loads(f.read())


for k in d_str:
    for value in d_str[k]:
        d[k].append(value)


for tag in d:
    # print(item,d[item])
    # print(len(d[item]))
    for i in range(0, len(d[tag])):
        print(tag, d[tag][i])
        db.tag(d[tag][i], tag)

d = defaultdict(list)
d_json_file = os.path.join(basepath, "gif_tagged.json")
if not os.path.exists(d_json_file):
    with open(d_json_file, "w") as f:
        pass

else:
    with open(d_json_file) as f:
        d_str = json.loads(f.read())


for k in d_str:
    for value in d_str[k]:
        print(k, value)
        d[k].append(value)

print("................")
for tag in d:
    print(tag)
    print(len(d[tag]))
    for i in range(0, len(d[tag])):
        print(tag, d[tag][i])

res = db.fetch_gif("woi")
if res:
    print(res)
    print(type(res))
    for item in res:
        print(item)
        #print(type(item))
    print('rnd')
    print(random.choice(res))
else:
    print("no res")
