import csv
from yanyan_GetStatus import bedwars_status

def allreset_session():
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        uuid_list = []
        for i, item in enumerate(data):
            split_item = item.split(",")
            if i != len(data)-1:
                uuid_list.append(split_item[58])
    
    return_text = "Reset All Session!"
    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        for uuid in uuid_list:
            status = bedwars_status(False, uuid)
            if status[0] != True:
                writer.writerow(status)
            else:
                return_text = "Error (Possibilities of API Key Error)\nhttps://developer.hypixel.net/dashboard/"
    return return_text
