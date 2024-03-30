# import requests
# import json
import csv

# def getinfo(call):
#     r = requests.get(call,timeout=10)
#     return r.json()
# with open('./Cheater/Players.json', 'r',) as e:
#     data = json.load(e)

# print(len(data))
# datas = list(set(data))
# print(len(datas))
# print(datas[0])
# write = []
# for item in datas:
#     write.append(f"{item}")

# with open('./Players.json', 'w') as f:
#     json.dump(datas, f, indent=4)

with open("./Cheater/Datas.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    # print(headers[28])
    # print(headers[27])

    # print(headers[37])
    # print(headers[32])

    # print(headers[17])
    # print(headers[18])

    # print(headers[6])
    # print(headers[1])

    # print(headers[28])
    # print(headers[6])

    # print(headers[31])
    # print(headers[6])

    # print(headers[17])
    # print(headers[6])
    new_csv_data = []
    for i, data in enumerate(csv_reader):
        if i != 0:
            data = [float(s) for s in data]
            data[38] = int(data[38])
            for num in [27, 32, 18, 6]:
                if data[num] == 0:
                    data[num] = 1
            # if data[28] / data[27] <= 1 and data[37] / data[32] <= 1 and data[17] / data[18] <= 1 and data[6] <= 30 and data[1] <= 1305 and data[28] / data[6] >= 7.5 and data[31] / data[6] >= 6.5 and data[17] / data[6] >= 20:
            #     # print(data)
            #     pass
            # if data[6] <= 30 and data[1] <= 1305:
            #     if (data[28] / data[27] <= 1 or data[37] / data[32] <= 1 or data[17] / data[18] <= 1) and (data[28] / data[6] >= 7.5 or data[31] / data[6] >= 6.5 or data[17] / data[6] >= 20):
            #         print(data)
            for j in [data[28] / data[27], data[37] / data[32], data[17] / data[18], data[28] / data[6], data[31] / data[6], data[17] / data[6]]:
                data.append(j)
            new_csv_data.append(data)
# print(new_csv_data)
# print(header)

with open('./Cheater/Data2.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(new_csv_data)