import requests
import json
import csv

def getinfo(call):
    r = requests.get(call,timeout=10)
    return r.json()
# with open('./Cheater/Players.json', 'r',) as e:
#     data = json.load(e)

# print(len(data))
# datas = list(set(data))
# print(len(datas))
# print(datas[0])
# write = []
# for item in datas:
#     write.append(f"{item}")

# with open('./Players.json', 'w') as f:
#     json.dump(datas, f, indent=4)

# with open("./Cheater/Datas.csv", mode='r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
    # print(headers[28])
    # print(headers[27])

    # print(headers[37])
    # print(headers[32])

    # print(headers[17])
    # print(headers[18])

    # print(headers[6])
    # print(headers[1])

    # print(headers[28])
    # print(headers[6])

    # print(headers[31])
    # print(headers[6])

    # print(headers[17])
    # print(headers[6])
    # new_csv_data = []
    # for i, data in enumerate(csv_reader):
    #     if i != 0:
    #         data = [float(s) for s in data]
    #         data[38] = int(data[38])
    #         for num in [27, 32, 18, 6]:
    #             if data[num] == 0:
    #                 data[num] = 1
            # if data[28] / data[27] <= 1 and data[37] / data[32] <= 1 and data[17] / data[18] <= 1 and data[6] <= 30 and data[1] <= 1305 and data[28] / data[6] >= 7.5 and data[31] / data[6] >= 6.5 and data[17] / data[6] >= 20:
            #     # print(data)
            #     pass
            # if data[6] <= 30 and data[1] <= 1305:
            #     if (data[28] / data[27] <= 1 or data[37] / data[32] <= 1 or data[17] / data[18] <= 1) and (data[28] / data[6] >= 7.5 or data[31] / data[6] >= 6.5 or data[17] / data[6] >= 20):
            #         print(data)
            # for j in [data[28] / data[27], data[37] / data[32], data[17] / data[18], data[28] / data[6], data[31] / data[6], data[17] / data[6]]:
            #     data.append(j)
            # new_csv_data.append(data)
# print(new_csv_data)
# print(header)

# with open('./Cheater/Data2.csv', 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(header)
#     writer.writerows(new_csv_data)


    # "JustElwai",
    # "sushiricerolll",
    # "DaBoringBread",
    # "TushieChawChaw",
    # "DDexter75",
    # "ChromeHeart_",
    # "Beserk_warrior",
    # "pfidoar12345",
    # "duonutti",
    # "Hypertopia",
    # "PANPAIYA",
    # "Squeezjoos123",
    # "94Jason269",
    # "Jim0913",
    # "Aiden0P9",
    # "Mobzzzz",
    # "PRO53013",
    # "edwinTSAI",
    # "Clutched_Yt",
    # "lrivex",
    # "AKX47__",
    # "jinho0405",
    # "Chris56719908",
    # "James_24",
    # "TheRealWholsYou",
    # "Ko6587568",
    # "Freezee21",
    # "hindv",
    # "trizzynokizzy",
    # "ColorBun",
    # "Killah121_",
    # "riasaki",
    # "Jairoooo",
    # "dalroon",
    # "LeoHot",
    # "savagepickle212",
    # "Active3112",
    # "SafeKoala926684",
    # "Purple_Smile",
    # "SaFeJ",
    # "odqsi",
    # "SRJP15",
    # "Kayzs",
    # "slm133",
    # "Edolak",
    # "EnderMite980",
    # "UnsafeBigfoot0",
    # "niffler29",
    # "SuperDanOrz",
    # "NADeath",
    # "porkiebibs",
    # "sebasaardbei",
    # "ikickdogs",
    # "Tizery",
    # "mosterXD",
    # "MushyMun",
    # "NemoinABottle",
    # "Bumsickle42",
    # "BlueRum",
    # "Commander_Keen11",
    # "poeitie",
    # "ssei_",
    # "MrMellowYellow",
    # "kkojiee",
    # "MrZZombie",
    # "Nulce",
    # "Amvoo",
    # "FoxyQHeart",
    # "Sams_GamingYT",
    # "Dragonw11",
    # "AciDicDog",
    # "beonmf",
    # "NotSold",
    # "Shockwave642",
    # "luvrachael",
    # "arrhona",
    # "IDontHitDingers",
    # "Dest1050",
    # "VVdog1234lol",
    # "ohRyderBoi",
    # "Logan_5956",
    # "xCatarsiss",
    # "A_S4",
    # "melerper",
    # "Galaxy_Dragon048",
    # "bihz",
    # "Depressoangel20",
    # "Lpbeastmode",
    # "PHY1225",
    # "ReturnError",
    # "Schoren130",
    # "Jhit_Slim3",
    # "niffler29",
    # "NinjaShadow40",
    # "Squandot",
    # "Charts",
    # "pigmyseal",
    # "melerper",
    # "RYE888",
    # "Kabimixbum",
    # "L_Bear08",
    # "Ssssgj",
    # "yigitcom",
    # "geofnfJ",
    # "storm438371",
    # "Ryu_pikt",
    # "melonsider",
    # "Mert14532013",
    # "TAVUKLAR123",
    # "wertyo0",
    # "Speedgamer1223",
    # "ltzJuliusMC",
    # "Razboi27",
    # "tjdcks2010",
    # "Mepleyz",
    # "IDieBclmLagging",
    # "ostonyso",
    # "Luke10Verse18",
    # "Luiwui777",
    # "YGold0816",
    # "PotatoSama_",
    # "FLEXBOSS333",
    # "BBDB33",
    # "MrFishyKing",
    # "DRIP_GOKU_318",
    # "Schlawotto",
    # "GamerPhil12",
    # "tougarashi1229",
    # "DimiTree2k",
    # "ElektroNerd1",
    # "morimoripower",
    # "WyvernHere",
    # "AWhite001",
    # "XXlmLazyPandaXX",

# with open('./Cheater/MCID_player.json', 'r',) as e:
#     data = json.load(e)
# for id in data:
#     name_link = f"https://api.mojang.com/users/profiles/minecraft/{id}"
#     try:
#         info = getinfo(name_link)
#     except requests.exceptions.JSONDecodeError:
#         pass
#     if info != None and "id" in info:
#         uuid = info["id"]
#         print(f'"{uuid}",')

with open('./Cheater/Cheaters.json', 'r',) as e:
    data = json.load(e)
with open('./Cheater/Players.json', 'r',) as e:
    data2 = json.load(e)
for id in data:
    if id in data2:
        print("aa")