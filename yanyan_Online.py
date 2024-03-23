import requests
import os
from dotenv import load_dotenv
import json
import time

def getinfo(call):
    r = requests.get(call,timeout=10)
    return r.json()

def get_online_list():
    with open('./player.csv', 'r',) as e:
        players = []
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and i != 0:
                players.append(item_data[0])

    with open('status.json') as f:
            di = json.load(f)

    ut = time.time()
    if ut - di["callstart"] >= 300:
        di["callstart"] = ut
        di["call"] = 0
    di["call"] += 1

    with open('status.json', 'w') as f:
        json.dump(di, f)

    with open('api.json') as f:
        tokens = json.load(f)
        
    API_KEY = tokens["HYPIXEL_TOKEN_0"]
    if di["call"] >= 270:
        if di["api_num"] == 0:
            API_KEY = tokens["HYPIXEL_TOKEN_1"]
            di["api_num"] = 1
        elif di["api_num"] == 1:
            API_KEY = tokens["HYPIXEL_TOKEN_2"]
            di["api_num"] = 2
        elif di["api_num"] == 2:
            API_KEY = tokens["HYPIXEL_TOKEN_0"]
            di["api_num"] = 0
        di["call"] = 0
        with open('status.json', 'w') as f:
            json.dump(di, f)
    online_list = []
    offline_list = []
    for item in players:
        name_link = f"https://api.mojang.com/users/profiles/minecraft/{item}"
        uuid = getinfo(name_link)
        if "id" in uuid:
            uuid = uuid["id"]
            uuid_link = f"https://api.hypixel.net/v2/status?key={API_KEY}&uuid={uuid}"
            data_dic = getinfo(uuid_link)
            if data_dic['success'] and data_dic["session"]["online"]:
                online_list.append(item)
            else:
                offline_list.append(item)
        else:
            offline_list.append(item)
    return [online_list, offline_list]

# print(get_online_list())