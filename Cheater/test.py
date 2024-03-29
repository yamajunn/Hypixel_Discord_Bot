import requests
import json

def getinfo(call):
    r = requests.get(call,timeout=10)
    return r.json()
with open('./Cheater/Players.json', 'r',) as e:
    data = json.load(e)

print(len(data))
datas = list(set(data))
print(len(datas))
print(datas[0])
write = []
for item in datas:
    write.append(f"{item}")

with open('./Players.json', 'w') as f:
    json.dump(datas, f, indent=4)