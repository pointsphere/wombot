import os
from collections import defaultdict
import json

from pathlib import Path


basepath = Path().absolute()

gif_sort_file = os.path.join(basepath, "gif_sort.py")
with open(gif_sort_file) as file:
    pass
    # bbb_set = set(line.strip() for line in file)


taglist = dir()
for item in taglist:
    if item not in ["Path", "os"]:
        if not item.startswith("_"):
            print(item)
            try:
                print(item[0])
            except Exception as e:
                print(e)


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


for item in d:
    # print(item,d[item])
    # print(len(d[item]))
    for i in range(0, len(d[item]) - 1):
        print(item, d[item][i])
