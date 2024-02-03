def player_list():
    with open('./player.csv', 'r',) as e:
        players = []
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and i != 0:
                players.append(item_data[0])
        players.append(f"**Total {len(data)}**")
    return players