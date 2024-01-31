import csv

def delete_player(name):
    with open('./player.csv', 'r',) as e:
        player_data = []
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and item_data[0] != name:
                player_data.append(item_data)

    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        for item in player_data:
            writer.writerow(item)