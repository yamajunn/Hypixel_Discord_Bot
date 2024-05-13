import time
def get_online():
    with open('./player.csv', 'r',) as e:
        onlines = ""
        update_onlines = ""
        offlines = ""
        data = e.read()
        data = data.split("\n")
        total = len(data)
        data = sorted(data)
        for index, s in enumerate(data):
            if s[0:4] == "MCID":
                del data[index]
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != 0:
                player_name = ""
                for name in list(item_data[0]):
                    if name == "_":
                        player_name += "\_"
                    else:
                        player_name += name
                if item_data[25] == "True":
                    onlines += f"🟢 [{item_data[24]}☆] **{player_name}**\r"
                elif time.time() - int(float(item_data[32])) <= 300:
                    update_onlines += f"🟡 [{item_data[24]}☆] **{player_name}**\r"
                else:
                    offlines += f"🔴 [{item_data[24]}☆] {player_name}\r"
    return [onlines, update_onlines, offlines, total]