import requests
import os
import pprint
import json
import time

def bedwars_status(bool, name):
    try:
        def getinfo(call):
            r = requests.get(call,timeout=10)
            return r.json()
        
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
        if di["call"] >= 290:
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

        if bool:
            name_link = f"https://api.mojang.com/users/profiles/minecraft/{name}"
            uuid = getinfo(name_link)["id"]
            uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        else:
            uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={name}"
            uuid = name

        data_dic = getinfo(uuid_link)
    except KeyError:
        return [True, "API key Error\nhttps://developer.hypixel.net/dashboard/", name]
    # print(data_dic)
    # pprint.pprint(data_dic)
    data_list = []
    if "player" in data_dic and data_dic["player"] != None:
        if "displayname" in data_dic["player"]:
            data_list.append(data_dic["player"]['displayname'])
        if data_dic["success"] == True:
            if data_dic["player"] != None:
                dic_list = ['wins_bedwars', 'losses_bedwars', 
                            'castle_wins_bedwars','castle_beds_lost_bedwars',
                            'eight_one_wins_bedwars','eight_one_losses_bedwars',
                            'eight_two_armed_wins_bedwars','eight_two_armed_losses_bedwars',
                            'eight_two_lucky_wins_bedwars','eight_two_lucky_losses_bedwars',
                            'eight_two_rush_wins_bedwars','eight_two_rush_losses_bedwars',
                            'eight_two_ultimate_wins_bedwars','eight_two_ultimate_losses_bedwars',
                            'eight_two_underworld_wins_bedwars','eight_two_underworld_losses_bedwars',
                            'eight_two_wins_bedwars','eight_two_losses_bedwars',
                            'eight_two_voidless_wins_bedwars','eight_two_voidless_losses_bedwars',
                            'four_four_armed_wins_bedwars','four_four_armed_losses_bedwars',
                            'four_four_wins_bedwars','four_four_losses_bedwars',
                            'four_four_lucky_wins_bedwars','four_four_lucky_losses_bedwars',
                            'four_four_rush_wins_bedwars','four_four_rush_losses_bedwars',
                            'four_four_swap_wins_bedwars','four_four_swap_losses_bedwars',
                            'four_four_ultimate_wins_bedwars','four_four_ultimate_losses_bedwars',
                            'four_four_underworld_wins_bedwars','four_four_underworld_losses_bedwars',
                            'four_four_voidless_wins_bedwars','four_four_voidless_losses_bedwars',
                            'four_three_wins_bedwars','four_three_losses_bedwars',
                            'tourney_bedwars_eight_two_0_wins_bedwars','tourney_bedwars_eight_two_0_losses_bedwars',
                            'tourney_bedwars_eight_two_1_wins_bedwars','tourney_bedwars_eight_two_1_losses_bedwars',
                            'two_four_wins_bedwars','two_four_losses_bedwars',
                            'winstreak',
                            'final_deaths_bedwars','final_kills_bedwars',
                            'eight_one_final_deaths_bedwars','eight_one_final_kills_bedwars',
                            'eight_two_final_deaths_bedwars','eight_two_final_kills_bedwars',
                            'four_three_final_deaths_bedwars','four_three_final_kills_bedwars',
                            'four_four_final_deaths_bedwars','four_four_final_kills_bedwars',
                            'two_four_final_deaths_bedwars','two_four_final_kills_bedwars',
                            ]
                for item in dic_list:
                    if item in data_dic["player"]["stats"]["Bedwars"]:
                        data_list.append(data_dic["player"]["stats"]["Bedwars"][item])
                    else:
                        data_list.append(0)

                data_list.append(uuid)

                if "monthlyPackageRank" in data_dic["player"] and data_dic["player"]['monthlyPackageRank'] != "NONE":
                    data_list.append(data_dic["player"]['monthlyPackageRank'])
                elif "newPackageRank" in data_dic["player"]:
                    data_list.append(data_dic["player"]['newPackageRank'])
                else:
                    data_list.append("NONE")
                data_list.append(data_dic["player"]['achievements']['bedwars_level'])
                return data_list
            else:
                return [True, "Error : None player data", name]
        else:
            return [True, "Error : Status not Success", name]
    else:
        return [True, "API Key Error\nhttps://developer.hypixel.net/dashboard/", name]
    
# print(bedwars_status(True, "Gokiton"))