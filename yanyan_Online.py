import requests
import os
from dotenv import load_dotenv

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

    load_dotenv()
    API_KEY = os.getenv("HYPIXEL_TOKEN")
    online_list = []
    offline_list = []
    for item in players:
        name_link = f"https://api.mojang.com/users/profiles/minecraft/{item}"
        uuid = getinfo(name_link)["id"]
        uuid_link = f"https://api.hypixel.net/v2/status?key={API_KEY}&uuid={uuid}"
        data_dic = getinfo(uuid_link)
        if data_dic['success'] and data_dic["session"]["online"]:
            online_list.append(item)
        else:
            offline_list.append(item)
    return [online_list, offline_list]

# print(get_online_list())