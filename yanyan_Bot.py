import discord
from discord import app_commands
from discord.ext import tasks
from dotenv import load_dotenv
import dotenv
import json
import time
import collections

from yanyan_AddPlayer import add_player
from yanyan_CheckStatus import check_status
from yanyan_ResetSession import reset_session
from yanyan_All_ResetSession import allreset_session
from yanyan_DeletePlayer import delete_player
from yanyan_PlayerList import player_list
from yanyan_Online import get_online_list
from yanyan_GetOnline import get_online
from yanyan_AI import judgment_cheater

dotenv_file = dotenv.find_dotenv()
with open('api.json') as f:
    tokens = json.load(f)
TOKEN = tokens["DISCORD_TOKEN"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Logged in as hypixel status")
    await tree.sync() #  コマンドを同期
    print("command sync") #  コマンドを同期した事の確認
    await check_status()
    check_loop.start()
    with open('status.json') as f:
        di = json.load(f)
    di["status"] = "True"
    with open('status.json', 'w') as f:
        json.dump(di, f)


@tree.command(name="add",description="Add player")
async def add_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    add_return = await add_player(name)
    print(f"{add_return}")
    embed = discord.Embed(title=f"{add_return}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="delete",description="Delete player")
async def delete_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    delete_player(name)
    print(f"Success! delete {name}")
    embed = discord.Embed(title=f"Success! delete {name}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="list",description="Player list")
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players = player_list()
    players_text = ""
    for item in players:
        players_text = f"{players_text}{item}\n"
    print("player list")
    embed = discord.Embed(title="Player List",description=players_text,color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="output",description="Output player list")
@app_commands.checks.has_any_role(1200023227586596914)
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players = player_list()
    players = players[0:len(players)-1]
    embed = discord.Embed(description=players,color=0x0000ff)
    print("output")
    await interaction.followup.send(embed=embed)


@tree.command(name="input",description="Input player list")
@app_commands.checks.has_any_role(1200023227586596914)
async def list_command(interaction: discord.Interaction,players:str):
    await interaction.response.defer()
    players = players[1:len(players)-1].replace("'","").replace(" ","").split(",")
    text = ""
    for item in players:
        return_text = add_player(item)
        text = f"{text}\n{return_text}"
    embed = discord.Embed(description=text,color=0x0000ff)
    print("input")
    await interaction.followup.send(embed=embed)

@tree.command(name="data_output",description="Output Data")
@app_commands.checks.has_any_role(1200023227586596914)
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    print("data output")
    await interaction.followup.send(file=discord.File("./player.csv"))


@tree.command(name="reset",description="Reset player session")
@app_commands.checks.has_any_role(1200023227586596914)
async def reset_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    return_text = await reset_session(name)
    embed = discord.Embed(title=f"{return_text}",color=0x0000ff)
    print(f"{return_text}")
    await interaction.followup.send(embed=embed)


@tree.command(name="allreset",description="Reset sessions for all players")
@app_commands.checks.has_any_role(1200023227586596914)
async def allreset_command(interaction: discord.Interaction):
    await interaction.response.defer()
    return_text = await allreset_session()
    embed = discord.Embed(title="Reset everything",description=f"{return_text}",color=0x0000ff)
    print(f"{return_text}")
    await interaction.followup.send(embed=embed)


@tree.command(name="start",description="Tracker Start")
@app_commands.checks.has_any_role(1200023227586596914)
async def start_command(interaction: discord.Interaction):
    await interaction.response.defer()
    with open('status.json') as f:
        di = json.load(f)
    if di["status"] == "True":
        embed = discord.Embed(title="⚠️ Already started",color=0x0000ff)
    else:
        check_loop.start()
        di["status"] = "True"
        with open('status.json', 'wt') as f:
            json.dump(di, f)
        embed = discord.Embed(title="✅ Start tracker!",color=0x0000ff)
    print("start")
    await interaction.followup.send(embed=embed)


@tree.command(name="stop",description="Tracker Stop")
@app_commands.checks.has_any_role(1200023227586596914)
async def stop_command(interaction: discord.Interaction):
    await interaction.response.defer()
    with open('status.json') as f:
        di = json.load(f)
    if di["status"] == "True":
        check_loop.stop()
        di["status"] = "False"
        with open('status.json', 'wt') as f:
            json.dump(di, f)
        embed = discord.Embed(title="🛑 Stop tracker!",color=0x0000ff)
    else:
        embed = discord.Embed(title="⚠️ Already stopped",color=0x0000ff)
    print("stop")
    await interaction.followup.send(embed=embed)


@tree.command(name="token1",description="Enter Hypixel token (yan1)")
@app_commands.checks.has_any_role(1200023227586596914)
async def token1_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_0"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success! add token1",color=0x0000ff)
    print("add token0")
    await interaction.followup.send(embed=embed)

@tree.command(name="token2",description="Enter Hypixel token (goki)")
@app_commands.checks.has_any_role(1200023227586596914)
async def token2_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_1"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success! add token2",color=0x0000ff)
    print("add token1")
    await interaction.followup.send(embed=embed)

@tree.command(name="token3",description="Enter Hypixel token (yan2)")
@app_commands.checks.has_any_role(1200023227586596914)
async def token3_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_2"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success! add token3",color=0x0000ff)
    print("add token2")
    await interaction.followup.send(embed=embed)


@tree.command(name="online",description="Online player list")
@app_commands.checks.has_any_role(1200023227586596914)
async def online_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players_text = ""
    player_status = get_online_list()
    for item in player_status[0]:
        players_text = f"{players_text}🟢  {item}\n"
    for item in player_status[1]:
        players_text = f"{players_text}🔴  {item}\n"
    embed = discord.Embed(title="Player Status",description=players_text,color=0x0000ff)
    print("online list")
    await interaction.followup.send(embed=embed)

@tree.command(name="cheat",description="Check Cheater")
async def add_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    return_judgment = judgment_cheater(name)
    if return_judgment == 0:
        embed = discord.Embed(title=f"{name} is Cheater",color=0xff0000)
    else:
        embed = discord.Embed(title=f"{name} is Not Cheater",color=0x1DAF00)
    print(return_judgment)
    await interaction.followup.send(embed=embed)

# max 80 member
@tasks.loop(seconds=30)  # 何秒おきにステータスをチェックするか指定(今は30秒)
async def check_loop():
    load_dotenv()
    return_list = await check_status()
    game_mode = []
    for item in return_list:
        if len(item) == 10 and item[9] == "OK":
            if item[0] != 1 or item[0] != 2 and len(item) != 4:
                game_mode.append(item[0])
    if len(game_mode) != 0:
        party_list = [k for k, v in collections.Counter(game_mode).items() if v > 1]
        party_dic = {}
        for i, item in enumerate(return_list):
            if item[0] in party_list and len(item) != 4:
                if not item[0] in party_dic:
                    party_dic[item[0]] = [item]
                else:
                    party_dic[item[0]].append(item)
                # return_list[i][0] = item[0] + 8
        for key, item in party_dic.items():
            combine_list = [key+8]
            for list_item in item:
                for i in list_item[1:8]:
                    combine_list.append(i)
            combine_list.append(item[0][8])
            combine_list.append("OK")
            return_list.append(combine_list)
    channel = client.get_channel(1220168548136259634)
    message = await channel.fetch_message(1220627500535779360)
    online_list, update_online, offline_list, total = get_online()
    embed = discord.Embed(title="Online Player",description=f"{online_list}{update_online}\r{offline_list}\rtotal **{total}**",color=0x0000ff)
    await message.edit(embed=embed, content=f"**Last updated :** <t:{int(time.time())}:R>")
    for item in return_list:
        print(item)
        if (len(item) == 10 or len(item)%7 == 2) and item[len(item)-1] == "OK":
            if item[0] in [1,2]:
                channel_id = 1200281905174675577
            elif item[0] in [3,4]:
                channel_id = 1200281873973264435
            elif item[0] in [5,6]:
                channel_id = 1200281758084628520
            elif item[0] in [7,8]:
                channel_id = 1200947061038776443
            elif item[0] in [9,10]:
                channel_id = 1201526061570207795
            elif item[0] in [11,12]:
                channel_id = 1220221698629046324
            elif item[0] in [13,14]:
                channel_id = 1220221713791586385
            elif item[0] in [15,16]:
                channel_id = 1220221735216087121
            elif item[0] in [17,18]:
                channel_id = 1220221763967910059
            else:
                break
            channel = client.get_channel(channel_id)
            if item[0] in [1,2,3,4,5,6,7,8,9,10]:
                if item[0] % 2 == 1:
                    color=0x1DAF00
                    if int(item[3])+1 >= 50:
                        color=0x660099
                    embed = discord.Embed(title=f"🔷 [{item[5]}☆] {item[4]}{item[1]}",description=f"Won with **{item[2]}**　　time : **{int((time.time()-float(item[8]))//60)}:{int((time.time()-float(item[8])))%60}**\nWs : {item[3]} → **{int(item[3])+1}**\nSession FKDR : {item[7]} → **{item[6]}**",color=color)
                    await channel.send(embed=embed)
                    await channel.send(f"<t:{int(time.time())}:T> 　　<t:{int(time.time())}:R>")
                else:
                    color=0xff0000
                    if int(item[3])+1 >= 50:
                        color=0xffff00
                    embed = discord.Embed(title=f"🔻 [{item[5]}☆] {item[4]}{item[1]}",description=f"Lost with **{item[2]}**　　time : **{int((time.time()-float(item[8]))//60)}:{int((time.time()-float(item[8])))%60}**\nWs : {item[3]} → **{0}**\nSession FKDR : {item[7]} → **{item[6]}**",color=color)
                    await channel.send(embed=embed)
                    await channel.send(f"<t:{int(time.time())}:T>　　<t:{int(time.time())}:R>")
            elif item[0] in [11,12,13,14,15,16,17,18]:
                if item[0] % 2 == 1:
                    players_title = ""
                    mode = f"Won with **{item[2]}**"
                    players_description = ""
                    for j in range(len(item)//7):
                        players_title += f"🔷 [{item[j*7+5]}☆] {item[j*7+4]}{item[j*7+1]}\n"
                        players_description += f"**{item[j*7+1]}**\nWs : {item[j*7+3]} → **{int(item[j*7+3])+1}**\nSession FKDR : {item[j*7+7]} → **{item[j*7+6]}**\n\n"
                    embed = discord.Embed(title=players_title,description=f"{mode}\n\n{players_description}\ntime : **{int((time.time()-float(item[len(item)-2]))//60)}:{int((time.time()-float(item[len(item)-2]))%60)}**",color=0x1DAF00)
                    await channel.send(embed=embed)
                    await channel.send(f"<t:{int(time.time())}:T> 　　<t:{int(time.time())}:R>")
                else:
                    players_title = ""
                    mode = f"Lost with **{item[2]}**"
                    players_description = ""
                    for j in range(len(item)//7):
                        players_title += f"🔻 [{item[j*7+5]}☆] {item[j*7+4]}{item[j*7+1]}\n"
                        players_description += f"**{item[j*7+1]}**\nWs : {item[j*7+3]} → **{int(item[j*7+3])+1}**\nSession FKDR : {item[j*7+7]} → **{item[j*7+6]}**\n\n"
                    embed = discord.Embed(title=players_title,description=f"{mode}\n\n{players_description}\ntime : **{int((time.time()-float(item[len(item)-2]))//60)}:{int((time.time()-float(item[len(item)-2]))%60)}**",color=0xff0000)
                    await channel.send(embed=embed)
                    await channel.send(f"<t:{int(time.time())}:T> 　　<t:{int(time.time())}:R>")
        elif len(item) == 4 and item[len(item)-1] == "OK":
            channel = client.get_channel(1222520603525910598)
            embed = discord.Embed(title=f"[{item[2]}☆] {item[1]}{item[0]}",description=f"Started game",color=0x0099ff)
            await channel.send(embed=embed)
            await channel.send(f"<t:{int(time.time())}:T> 　　<t:{int(time.time())}:R>")
        elif item[1] == 'ApiKeyError':
            with open('status.json') as f:
                di = json.load(f)
            api_number = di['api_num']
            embed = discord.Embed(title=f"API has expired (number {api_number+1})\nhttps://developer.hypixel.net/dashboard/\n🛑 Stop tracker",color=0x0000ff)
            channel = client.get_channel(1200951245259686020)
            await channel.send(embed=embed)
            if api_number  == 1:
                user = await client.fetch_user(797350769250140161)
            else:
                user = await client.fetch_user(805317573511479306)
            mention = user.mention
            await channel.send(f"{mention}")
            with open('status.json') as f:
                di = json.load(f)
            if di["status"] == "True":
                check_loop.stop()
                di["status"] = "False"
                with open('status.json', 'wt') as f:
                    json.dump(di, f)
            print("stop")
            check_loop.stop()
        else:
            print(item)

client.run(TOKEN)  # \(o v o)/ ﾜｰｲ