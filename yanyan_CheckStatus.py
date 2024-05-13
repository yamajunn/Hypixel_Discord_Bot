from yanyan_GetStatus import bedwars_status
from yanyan_ChangeCsv import change_csv

async def check_status():
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
    return_list = []
    game_name = [
        'Solo','eight_one_losses_bedwars',
        'Doubles','eight_two_losses_bedwars',
        '3s','four_three_losses_bedwars',
        '4s','four_four_wins_bedwars',
        '4v4','two_four_losses_bedwars',
        "Ws",
        'final_deaths_bedwars','final_kills_bedwars',
        'eight_one_final_deaths_bedwars','eight_one_final_kills_bedwars',
        'eight_two_final_deaths_bedwars','eight_two_final_kills_bedwars',
        'four_three_final_deaths_bedwars','four_three_final_kills_bedwars',
        'four_four_final_deaths_bedwars','four_four_final_kills_bedwars',
        'two_four_final_deaths_bedwars','two_four_final_kills_bedwars',
        ]
    for i, item in enumerate(data):
        if i != 0 and i != len(data)-1:
            data_item = item.split(",")
            status = await bedwars_status(False, data_item[22])
            if status[0] == True and status[1] == "Key throttle":
                continue
            if status[0] == True and status[1] == "ApiKeyError":
                return_list = [status]
                break
            str_status = list(map(str, status))
            if status[0] != True and (str_status[1:10] != data_item[1:10] or status[25] != data_item[25] or status[32] != data_item[32]):
                for i, item in enumerate(str_status):
                    if item != data_item[i]:
                        if i in [1,2, 3,4, 5,6, 7,8, 9,10, 25, 26]:  # solo, doubles, 3s, 4s, 4v 以外は排除
                            rank = ""
                            if str_status[23] == "SUPERSTAR":
                                rank = "[MVP++] "
                            elif str_status[23] == "MVP_PLUS":
                                rank = "[MVP+] "
                            elif str_status[23] == "MVP":
                                rank = "[MVP] "
                            elif str_status[23] == "VIP_PLUS":
                                rank = "[VIP+] "
                            elif str_status[23] == "VIP":
                                rank = "[VIP] "

                            if not i in [25, 26]:
                                fkdr = 0
                                try:
                                    fkdr = round((int(str_status[i+(i%2)+11])-int(data_item[i+(i%2)+11])) / (int(str_status[i+(i%2)+10])-int(data_item[i+(i%2)+10])), 2)
                                except ZeroDivisionError:
                                    fkdr = int(str_status[i+(i%2)+11])-int(data_item[i+(i%2)+11])
                                return_list.append([i, data_item[0], game_name[i+(i%2-1)-1], data_item[11], rank, str_status[24], fkdr, data_item[(i+(i%2))//2+26], data_item[32], "OK"])
                                await change_csv(data_item[22],i % 2, data_item[11],fkdr, False, i)
                            elif i == 25:
                                await change_csv(data_item[22], None, None, None, True, None)
                            else:
                                await change_csv(data_item[22], None, None, None, True, None)
                                return_list.append([data_item[0], rank, str_status[24], "OK"])
            elif status[0] == True:
                return_list = [status]
    return return_list
# check_status()