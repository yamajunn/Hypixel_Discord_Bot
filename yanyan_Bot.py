import discord
from discord import app_commands
from discord.ext import tasks
import os
from dotenv import load_dotenv
import dotenv
import json
import datetime
import pytz
import csv
from datetime import time

from yanyan_AddPlayer import add_player
from yanyan_CheckStatus import check_status
from yanyan_ResetSession import reset_session
from yanyan_All_ResetSession import allreset_session
from yanyan_DeletePlayer import delete_player
from yanyan_PlayerList import player_list
from yanyan_Online import get_online_list

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
    check_status()
    my_background_task.start()
    with open('status.json') as f:
        di = json.load(f)
    di["status"] = "True"
    with open('status.json', 'w') as f:
        json.dump(di, f)


@tree.command(name="add",description="Add player")
async def add_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    add_return = add_player(name)
    embed = discord.Embed(title=f"{add_return}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="delete",description="Delete player")
async def delete_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    delete_player(name)
    embed = discord.Embed(title=f"Success! delete {name}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="list",description="Player list")
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players = player_list()
    players_text = ""
    for item in players:
        players_text = f"{players_text}{item}\n"
    embed = discord.Embed(title="Player List",description=players_text,color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="output",description="Output player list")
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players = player_list()
    players = players[0:len(players)-1]
    embed = discord.Embed(description=players,color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="input",description="Input player list")
async def list_command(interaction: discord.Interaction,players:str):
    await interaction.response.defer()
    players = players[1:len(players)-1].replace("'","").replace(" ","").split(",")
    text = ""
    for item in players:
        return_text = add_player(item)
        text = f"{text}\n{return_text}"
    embed = discord.Embed(description=text,color=0x0000ff)
    await interaction.followup.send(embed=embed)

@tree.command(name="data_output",description="Output Data")
async def list_command(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send(file=discord.File("./player.csv"))


@tree.command(name="reset",description="Reset player session")
async def reset_command(interaction: discord.Interaction,name:str):
    await interaction.response.defer()
    return_text = reset_session(name)
    embed = discord.Embed(title=f"{return_text}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="allreset",description="Reset sessions for all players")
async def allreset_command(interaction: discord.Interaction):
    await interaction.response.defer()
    return_text = allreset_session()
    embed = discord.Embed(title="Reset everything",description=f"{return_text}",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="start",description="Tracker Start")
async def start_command(interaction: discord.Interaction):
    await interaction.response.defer()
    with open('status.json') as f:
        di = json.load(f)
    if di["status"] == "True":
        embed = discord.Embed(title="⚠️ Already started",color=0x0000ff)
    else:
        my_background_task.start()
        di["status"] = "True"
        with open('status.json', 'wt') as f:
            json.dump(di, f)
        embed = discord.Embed(title="✅ Start tracker!",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="stop",description="Tracker Stop")
async def stop_command(interaction: discord.Interaction):
    await interaction.response.defer()
    with open('status.json') as f:
        di = json.load(f)
    if di["status"] == "True":
        my_background_task.stop()
        di["status"] = "False"
        with open('status.json', 'wt') as f:
            json.dump(di, f)
        embed = discord.Embed(title="🛑 Stop tracker!",color=0x0000ff)
    else:
        embed = discord.Embed(title="⚠️ Already stopped",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="token1",description="Enter Hypixel token")
async def token1_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_0"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success!",color=0x0000ff)
    await interaction.followup.send(embed=embed)

@tree.command(name="token2",description="Enter Hypixel token")
async def token2_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_1"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success!",color=0x0000ff)
    await interaction.followup.send(embed=embed)

@tree.command(name="token3",description="Enter Hypixel token")
async def token3_command(interaction: discord.Interaction,token:str):
    await interaction.response.defer()
    with open('api.json') as f:
        tokens = json.load(f)
    tokens["HYPIXEL_TOKEN_2"] = token
    with open('api.json', 'w') as f:
        json.dump(tokens, f)
    embed = discord.Embed(title=f"Success!",color=0x0000ff)
    await interaction.followup.send(embed=embed)


@tree.command(name="online",description="Online player list")
async def online_command(interaction: discord.Interaction):
    await interaction.response.defer()
    players_text = ""
    player_status = get_online_list()
    for item in player_status[0]:
        players_text = f"{players_text}🟢  {item}\n"
    for item in player_status[1]:
        players_text = f"{players_text}🔴  {item}\n"
    embed = discord.Embed(title="Player Status",description=players_text,color=0x0000ff)
    await interaction.followup.send(embed=embed)

# max 80 member
@tasks.loop(seconds=30)  # 何秒おきにステータスをチェックするか指定(今は30秒)
async def my_background_task():
    load_dotenv()
    return_list = check_status()
    if return_list != ["API Key Error\nhttps://developer.hypixel.net/dashboard/"]:
        # channel_id = 1200281946643759145
        print(return_list)
        for item in return_list:
            if item[0] in [5,6]:
                channel_id = 1200281905174675577
            elif item[0] in [17,18]:
                channel_id = 1200281873973264435
            elif item[0] in [23,24]:
                channel_id = 1200947061038776443
            elif item[0] in [37,38]:
                channel_id = 1200281758084628520
            elif item[0] in [43,44]:
                channel_id = 1201526061570207795
            else:
                break
            
            channel = client.get_channel(channel_id)
            now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).time()


            if item[0] % 2 == 1:
                embed = discord.Embed(title=f"🔷 [{item[5]}☆] {item[4]}{item[1]}",description=f"     Won with **{item[2]}**\n     Ws : {item[3]} → **{int(item[3])+1}**\n     Session FKDR : {item[7]} → **{item[6]}**\n{now.hour}:{now.minute}",color=0x00ff00)
                await channel.send(embed=embed)
            else:
                embed = discord.Embed(title=f"🔻 [{item[5]}☆] {item[4]}{item[1]}",description=f"     Lost with **{item[2]}**\n     Ws : {item[3]} → **{0}**\n     Session FKDR : {item[7]} → **{item[6]}**\n{now.hour}:{now.minute}",color=0xff0000)
                await channel.send(embed=embed)
    else:
        with open('status.json') as f:
            di = json.load(f)
        embed = discord.Embed(title=f"API has expired (number {di['api_num']+1})\nhttps://developer.hypixel.net/dashboard/\n🛑 Stop tracker",color=0x0000ff)
        channel = client.get_channel(1200951245259686020)
        await channel.send(embed=embed)
        my_background_task.stop()


client.run(TOKEN)  # \(0 w 0)/ ﾜｰｲ