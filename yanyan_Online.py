from yanyan_GetStatus import bedwars_status

def get_online_list():
    with open('./player.csv', 'r',) as e:
        players = []
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and i != 0:
                players.append(item_data[0])

    return_list = []
    offline_list = []
    for name in players:
        data = bedwars_status(True, name)
        if data[0] != True and len(data) == 63 and data[62] - data[61] > 0:
            return_list.append(name)
        else:
            offline_list.append(name)
    return [return_list, offline_list]

# print(get_online_list())