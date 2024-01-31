import csv
from yanyan_GetStatus import bedwars_status

def change_csv(uuid):
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        csv_list = []
        session = []
        for i, item in enumerate(data):
            split_item = item.split(",")
            if i != len(data)-1 and split_item[58] != uuid:
                csv_list.append(split_item)
            elif i != len(data)-1 and split_item[58] == uuid:
                session = list(split_item[46:56])

    with open('./player.csv', 'w', newline="") as e:
        writer = csv.writer(e)
        writer.writerows(csv_list)
        status = bedwars_status(False, uuid)
        if status[0] != True:
            status[46:56] = session
            writer.writerow(status)