import csv
from yanyan_GetStatus import bedwars_status
import time

async def change_csv(uuid, num, ws, fkdr, online, mode):
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        csv_list = []
        session = []
        for i, item in enumerate(data):
            split_item = item.split(",")
            if i != len(data)-1 and split_item[22] != uuid:
                csv_list.append(split_item)
            elif i != len(data)-1 and split_item[22] == uuid:
                session = list(split_item[11:21])
                fkdrs = list(split_item[27:32])

    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerows(csv_list)
        status = await bedwars_status(False, uuid)
        if status[0] != True:
            status[11:21] = session
            if not online:
                if num == 1:
                    status[11] = int(ws)+1
                else:
                    status[11] = 0
                fkdrs[(mode + mode % 2)//2-1] = fkdr
                for item in fkdrs:
                    status.append(item)
                status.append(time.time())
            else:
                for item in fkdrs:
                    status.append(item)
                status.append(time.time())
            writer.writerow(status)