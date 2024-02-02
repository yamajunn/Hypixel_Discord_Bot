from yanyan_GetStatus import bedwars_status
from yanyan_ChangeCsv import change_csv

def check_status():
    with open('./player.csv', 'r',) as e:
        data = e.read()
        data = data.split("\n")
        return_list = []
        game_name = ['WIN', 'LOSS', 
                            'Castle','castle_beds_lost_bedwars',
                            'Solo','eight_one_losses_bedwars',
                            'Armed Doubles','eight_two_armed_losses_bedwars',
                            'Lucky Doubles','eight_two_lucky_losses_bedwars',
                            'Rush Doubles','eight_two_rush_losses_bedwars',
                            'Ultimate Doubles','eight_two_ultimate_losses_bedwars',
                            'Underworld Doubles','eight_two_underworld_losses_bedwars',
                            'Doubles','eight_two_losses_bedwars',
                            'Voidless Doubles','eight_two_voidless_losses_bedwars',
                            'Armed 4s','four_four_armed_losses_bedwars',
                            '4s','four_four_wins_bedwars',
                            'Lucky 4s','four_four_lucky_losses_bedwars',
                            'Rush 4s','four_four_rush_losses_bedwars',
                            'Swap 4s','four_four_swap_wins_bedwars',
                            'Ultimate 4s','four_four_ultimate_losses_bedwars',
                            'Underworld 4s','four_four_underworld_losses_bedwars',
                            'Voidless 4s','four_four_voidless_losses_bedwars',
                            '3s','four_three_losses_bedwars',
                            'First Tourney Doubles','tourney_bedwars_eight_two_0_losses_bedwars',
                            'Second Tourney Doubles','tourney_bedwars_eight_two_1_losses_bedwars',
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
                status = bedwars_status(False, data_item[58])
                str_status = list(map(str, status))
                if status[0] != True and str_status[1:46] != data_item[1:46]:
                    for i, item in enumerate(str_status):
                        if item != data_item[i]:
                            if i in [5,6, 17,18, 23,24, 37,38, 43,44]:  # solo, duo, 3s, 4s, 4v 以外は排除
                                rank = ""
                                if str_status[59] == "SUPERSTAR":
                                    rank = "[MVP++] "
                                elif str_status[59] == "MVP_PLUS":
                                    rank = "[MVP+] "
                                elif str_status[59] == "MVP":
                                    rank = "[MVP] "
                                elif str_status[59] == "VIP_PLUS":
                                    rank = "[VIP+] "
                                elif str_status[59] == "VIP":
                                    rank = "[VIP] "
                                fkdr = 0
                                try:
                                    if i+(i%2-1) == 1:
                                        fkdr = round((int(str_status[47])-int(data_item[47])) / (int(str_status[46])-int(data_item[46])), 2)
                                    elif i+(i%2-1) == 5:
                                        fkdr = round((int(str_status[49])-int(data_item[49])) / (int(str_status[48])-int(data_item[48])), 2)
                                    elif i+(i%2-1) == 17:
                                        fkdr = round((int(str_status[51])-int(data_item[51])) / (int(str_status[50])-int(data_item[50])), 2)
                                    elif i+(i%2-1) == 23:
                                        fkdr = round((int(str_status[53])-int(data_item[53])) / (int(str_status[52])-int(data_item[52])), 2)
                                    elif i+(i%2-1) == 37:
                                        fkdr = round((int(str_status[55])-int(data_item[55])) / (int(str_status[54])-int(data_item[54])), 2)
                                    elif i+(i%2-1) == 43:
                                        fkdr = round((int(str_status[57])-int(data_item[57])) / (int(str_status[56])-int(data_item[56])), 2)
                                except ZeroDivisionError:
                                    fkdr = 1
                                return_list.append([i, data_item[0], game_name[i+(i%2-1)-1], data_item[45], str_status[45], rank, str_status[60], fkdr])
                    change_csv(data_item[58])
                elif status[0] == True:
                    return_list = ["Error (Possibilities of API Key Error)\nhttps://developer.hypixel.net/dashboard/"]
    return return_list
check_status()