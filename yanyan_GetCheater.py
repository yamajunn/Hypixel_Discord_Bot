import time
import requests
import json
# karma,
# networkExp,
# bedwars_beds,
# bedwars_bedwars_challenger,
# bedwars_bedwars_killer,
# bedwars_collectors_edition,
# bedwars_level,
# bedwars_loot_box,
# bedwars_slumber_ticket_master,
# bedwars_wins,
# challenges,
# all_timeBEDWARS__defensive,
# BEDWARS__offensive,
# BEDWARS__support,
# Bedwars_openedChests,
# Experience,
# _items_purchased_bedwars,
# beds_broken_bedwars,
# beds_lost_bedwars,
# coins,
# deaths_bedwars,
# diamond_resources_collected_bedwars,
# emerald_resources_collected_bedwars,
# fall_deaths_bedwars,
# fall_final_deaths_bedwars,
# fall_final_kills_bedwars,
# fall_kills_bedwars,
# final_deaths_bedwars,
# final_kills_bedwars,
# games_played_bedwars,
# games_played_bedwars_1,
# kills_bedwars,
# losses_bedwars,
# void_deaths_bedwars,
# void_final_deaths_bedwars,
# void_final_kills_bedwars,
# void_kills_bedwars,
# wins_bedwars,
# Cheat,
# fkdr,
# wlr,
# bblr,
# fk_lev,
# bb_lev,
# kill_lev
dic_labels = [
    'karma',
    'networkExp',
    # 'newPackageRank',
    # 'particlePack',
    # 'playername',
    # 'questSettings',
    # 'rankPlusColor',
]
achievements = [
    'bedwars_beds',
    'bedwars_bedwars_challenger',
    'bedwars_bedwars_killer',
    'bedwars_collectors_edition',
    'bedwars_level',
    'bedwars_loot_box',
    'bedwars_slumber_ticket_master',
    'bedwars_wins',
]
challenges = [
    'challenges',
    'all_timeBEDWARS__defensive',
    'BEDWARS__offensive',
    'BEDWARS__support',
]
statuses = [
    'Bedwars_openedChests',
    'Experience',
    '_items_purchased_bedwars',
    # 'activeWoodType',
    'beds_broken_bedwars',
    'beds_lost_bedwars',
    'coins',
    'deaths_bedwars',
    'diamond_resources_collected_bedwars',
    'emerald_resources_collected_bedwars',
    'fall_deaths_bedwars',
    'fall_final_deaths_bedwars',
    'fall_final_kills_bedwars',
    'fall_kills_bedwars',
    # 'favourites_2',
    'final_deaths_bedwars',
    'final_kills_bedwars',
    'games_played_bedwars',
    'games_played_bedwars_1',
    'kills_bedwars',
    'losses_bedwars',
    'void_deaths_bedwars',
    'void_final_deaths_bedwars',
    'void_final_kills_bedwars',
    'void_kills_bedwars',
    'wins_bedwars',
]

with open('status.json') as f:
    di = json.load(f)
with open('api.json') as f:
    tokens = json.load(f)

# API_KEY = tokens[f"HYPIXEL_TOKEN_{di['api_num']}"]
API_KEY = tokens[f"HYPIXEL_TOKEN_1"]

def getinfo(call):
    r = requests.get(call,timeout=10)
    return r.json()

def get_cheater(name):

    name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"
    info = getinfo(name_link)
    get_uuid = ""
    if info != None:
        get_uuid = [info["id"]]

    # print(get_uuid)
    data_list = []
    for i, uuid in enumerate(get_uuid):
        uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        data_dic = getinfo(uuid_link)
        datas = []
        if "cause" in data_dic and data_dic["cause"] == "Key throttle":
            time.sleep(300)
        if data_dic is not None and "player" in data_dic and data_dic["player"] is not None:
            for dic_label in dic_labels:
                if dic_label in data_dic["player"]:
                    datas.append(data_dic["player"][dic_label])
                else:
                    datas.append(0)
            for achievement in achievements:
                if 'achievements' in data_dic["player"] and achievement in data_dic["player"]['achievements']:
                    datas.append(data_dic["player"]['achievements'][achievement])
                else:
                    datas.append(0)
            for challenge in challenges:
                if 'challenges' in data_dic["player"] and 'all_time' in data_dic["player"]['challenges'] and challenge in data_dic["player"]['challenges']['all_time']:
                    datas.append(data_dic["player"]['challenges']['all_time'][challenge])
                else:
                    datas.append(0)
            for stats in statuses:
                if 'stats' in data_dic["player"] and 'Bedwars' in data_dic["player"]['stats'] and stats in data_dic["player"]['stats']['Bedwars']:
                    datas.append(data_dic["player"]['stats']['Bedwars'][stats])
                else:
                    datas.append(0)
            for k in [27,32,18,6]:
                if datas[k] == 0:
                    datas[k] = 1
            for j in [datas[28] / datas[27], datas[37] / datas[32], datas[17] / datas[18], datas[28] / datas[6], datas[31] / datas[6], datas[17] / datas[6]]:
                datas.append(j)
            if not all(i == 0 for i in datas):
                data_list.append(datas)
                # print(f"{datas[0:len(datas)-1]}")
        else:
            print(i, data_dic)
    return data_list

# print(len(get_cheater("Gokiton")[0]))