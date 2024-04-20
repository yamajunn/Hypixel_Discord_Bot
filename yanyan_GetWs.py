def get_ws():
    with open('./player.csv', 'r',) as e:
        ws = ""
        data = e.read()
        data = data.split("\n")
        total = len(data)
        data = sorted(data)
        item_data = []
        for index, s in enumerate(data):
            if s[0:4] == "MCID":
                del data[index]
        for i, item in enumerate(data):
            if i != 0:
                item_data.append(item.split(","))
        item_data = sorted(item_data, reverse=True, key=lambda x: x[11])
        for i, item in enumerate(item_data):
            player_name = ""
            for name in list(item[0]):
                if name == "_":
                    player_name += "\_"
                else:
                    player_name += name
            ws += f"[{item[24]}☆] **{player_name}** ws: **{item[11]}**\r"
    return [ws, total]