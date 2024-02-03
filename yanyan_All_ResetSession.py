import csv
from yanyan_GetStatus import bedwars_status

def allreset_session():
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        uuid_list = []
        first = []
        for i, item in enumerate(data):
            split_item = item.split(",")
            if i == 0:
                first = split_item
            elif i != len(data)-1:
                uuid_list.append(split_item[58])
    
    return_text = ""
    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerow(first)
        for uuid in uuid_list:
            status = bedwars_status(False, uuid)
            if status[0] != True:
                writer.writerow(status)
                return_text = f"{return_text}Reset {status[0]} Session!\n"
            else:
                return_text = f"{return_text}{status[1]}({status[2]})\n"
    return return_text
