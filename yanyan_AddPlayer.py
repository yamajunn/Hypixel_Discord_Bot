import csv
from yanyan_GetStatus import bedwars_status

def add_player(name):
    with open('./player.csv', 'r',) as e:
        players = []
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != 0 and i != len(data)-1:
                players.append(item_data[0])
    if not name in players:
        with open('./player.csv', 'a', newline="") as e:
            writer = csv.writer(e)
            status = bedwars_status(True, name)
            if status[0] != True and not name in players:
                writer.writerow(status)
                return f"Success! add {name}"
            elif status[1] == "api key error":
                return "Error (Possibilities of API Key Error)\nhttps://developer.hypixel.net/dashboard/"
            else:
                return f"{name} is Error"
    else:
        return f"{name} has already been added."
# print(add_player("Gokiton"))