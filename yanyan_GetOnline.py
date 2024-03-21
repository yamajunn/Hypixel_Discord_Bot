def get_online():
    with open('./player.csv', 'r',) as e:
        onlines = ""
        offlines = ""
        data = e.read()
        data = data.split("\n")
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and i != 0:
                # rank = ""
                # if item_data[59] == "SUPERSTAR":
                #     rank = "[MVP++] "
                # elif item_data[59] == "MVP_PLUS":
                #     rank = "[MVP+] "
                # elif item_data[59] == "MVP":
                #     rank = "[MVP] "
                # elif item_data[59] == "VIP_PLUS":
                #     rank = "[VIP+] "
                # elif item_data[59] == "VIP":
                #     rank = "[VIP] "
                
                if item_data[61] == "True":
                    onlines += f"🟢    [{item_data[60]}☆]   {item_data[0]}\r"
                else:
                    offlines += f"🔴    [{item_data[60]}☆]   {item_data[0]}\r"
    return [onlines, offlines]