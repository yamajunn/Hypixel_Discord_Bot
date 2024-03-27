import csv
import time
from yanyan_GetStatus import bedwars_status

async def allreset_session():
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
                uuid_list.append(split_item[22])
    
    return_text = ""
    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerow(first)
        for i, uuid in enumerate(uuid_list):
            status = await bedwars_status(False, uuid)
            if status[0] != True:
                for j in range(5):
                    status.append(0)
                status.append(time.time())
                writer.writerow(status)
                return_text = f"{return_text}Reset {status[0]} Session!\n"
            else:
                return_text = f"{status[1]}({status[2]})\n"
    return return_text
