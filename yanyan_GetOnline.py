import time
def get_online():
    with open('./player.csv', 'r',) as e:
        onlines = ""
        update_onlines = ""
        offlines = ""
        data = e.read()
        data = data.split("\n")
        total = len(data)
        for i, item in enumerate(data):
            item_data = item.split(",")
            if i != len(data)-1 and i != 0:

                if item_data[25] == "True":
                    onlines += f"🟢　[{item_data[24]}☆]　**{item_data[0]}**\r"
                elif time.time() - int(float(item_data[32])) <= 300:
                    update_onlines += f"🟡　[{item_data[24]}☆]　**{item_data[0]}**\r"
                else:
                    offlines += f"🔴　[{item_data[24]}☆]　{item_data[0]}\r"
    return [onlines, update_onlines, offlines, total]