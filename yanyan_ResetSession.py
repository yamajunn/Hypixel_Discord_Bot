import csv
from yanyan_GetStatus import bedwars_status

async def reset_session(name):
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        csv_list = []
        for i, item in enumerate(data):
            split_item = item.split(",")
            if i != len(data)-1 and split_item[0] != name:
                csv_list.append(split_item)
    
    return_text = f"Reset {name} Session!"
    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerows(csv_list)
        status = await bedwars_status(True, name)
        if status[0] != True:
            status.append(0)
            writer.writerow(status)
        else:
            return_text = status[1]
    return return_text
