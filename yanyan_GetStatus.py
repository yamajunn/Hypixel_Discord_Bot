import requests
import os
import pprint
import json
import time
import aiohttp
import asyncio

async def bedwars_status(bool, name):
    async def getinfo(call):
        async with aiohttp.ClientSession() as session:
            async with session.get(call) as r:
                return await r.json()
    try:
        
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
            
        API_KEY = tokens[f"HYPIXEL_TOKEN_{di['api_num']}"]
        if di["call"] >= 140:
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
            info = await getinfo(name_link)
            if info != None:
                uuid = info["id"]
                uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
                # uuid_link = f"https://api.hypixel.net/recentgames?key={API_KEY}&uuid={uuid}"
        else:
            uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={name}"
            uuid = name

        data_dic = await getinfo(uuid_link)
    except KeyError:
        return [True, "ApiKeyError"]
    # print(data_dic)
    # pprint.pprint(data_dic)
    data_list = []
    if data_dic != None:
        if not ("cause" in data_dic and data_dic["cause"] == 'Invalid API key'):
            if not ("cause" in data_dic and data_dic["cause"] == "Key throttle"):
                if "player" in data_dic and data_dic["player"] != None:
                    if data_dic["success"] == True:
                        if "displayname" in data_dic["player"]:
                            data_list.append(data_dic["player"]['displayname'])
                        else:
                            data_list.append("Unknown")
                        dic_list = ['eight_one_wins_bedwars','eight_one_losses_bedwars',
                                    'eight_two_wins_bedwars','eight_two_losses_bedwars',
                                    'four_three_wins_bedwars','four_three_losses_bedwars',
                                    'four_four_wins_bedwars','four_four_losses_bedwars',
                                    'two_four_wins_bedwars','two_four_losses_bedwars',
                                    'winstreak',
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
                        
                        if 'achievements' in data_dic["player"] and "bedwars_level" in data_dic["player"]['achievements']:
                            data_list.append(data_dic["player"]['achievements']['bedwars_level'])
                        else:
                            data_list.append(0)
                        
                        if "lastLogin" in data_dic["player"] and "lastLogout" in data_dic["player"]:
                            if data_dic["player"]["lastLogout"] - data_dic["player"]["lastLogin"] >= 0:
                                data_list.append(False)
                            else:
                                data_list.append(True)
                        else:
                            data_list.append(False)
                        game_played = [
                            'eight_one_games_played_bedwars',
                            'eight_two_games_played_bedwars',
                            'four_three_games_played_bedwars',
                            'four_four_games_played_bedwars',
                            'two_four_games_played_bedwars'
                                    ]
                        # for queue in game_played:
                        #     if queue in data_dic["player"]["stats"]["Bedwars"]:
                        #         data_list.append(data_dic["player"]["stats"]["Bedwars"][queue])
                        #     else:
                        #         data_list.append(0)
                        if 'games_played_bedwars_1' in data_dic["player"]["stats"]["Bedwars"]:
                            data_list.append(data_dic["player"]["stats"]["Bedwars"]['games_played_bedwars_1'])
                        else:
                            data_list.append(0)
                        return data_list
                    else:
                        return [True, "Status not Success"]
                else:
                    return [True, f"None player data{data_dic}"]
            else:
                with open('status.json') as f:
                    di = json.load(f)
                if di["api_num"] == 0:
                    di["api_num"] = 1
                elif di["api_num"] == 1:
                    di["api_num"] = 2
                elif di["api_num"] == 2:
                    di["api_num"] = 0
                di["call"] = 0
                ut = time.time()
                di["callstart"] = ut
                with open('status.json', 'w') as f:
                    json.dump(di, f)
                return [True, f"Key throttle"]
        else:
            return [True, "ApiKeyError"]
    else:
        return [True, "None data"]
    
async def main():
    # 他のコード
    # result = await bedwars_status(True, "Gokiton")
    result = await bedwars_status(False, "1ced16db2bc54354917f7bf8382b8840")
    print(result)

# asyncio.run(main())