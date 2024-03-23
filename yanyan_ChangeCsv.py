import csv
from yanyan_GetStatus import bedwars_status

def change_csv(uuid, num, ws, fkdr, online, mode):
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
                session = list(split_item[12:21])
                fkdrs = list(split_item[26:31])

    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerows(csv_list)
        status = bedwars_status(False, uuid)
        if status[0] != True:
            status[12:21] = session
            if not online:
                if num == 1:
                    status[11] = int(ws)+1
                else:
                    status[11] = 0
                fkdrs[(mode + mode % 2)//2-1] = fkdr
                for item in fkdrs:
                    status.append(item)
            else:
                if status[25]:
                    status[25] = False
                else:
                    status[25] = True
                for item in fkdrs:
                    status.append(item)
            writer.writerow(status)