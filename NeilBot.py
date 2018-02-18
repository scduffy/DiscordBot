import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime
import urllib.request
import urllib.parse
import re

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot has connected.")

@client.event
async def on_message(message):
    #Gives the steam-connect for the Ark Server
    if message.content.upper() == "?ARK":
        await client.send_message(message.channel, "steam://connect/100.16.94.176:27015")
    # Tests to see if the bot is responding
    if message.content.upper() == "?TESTBOT":
        pinned_message = message
        await client.send_message(message.channel, "Responding.")
    # Gets the time until HQ
    if message.content.upper() == "?HQ":
        time = str(datetime.datetime.now())[11:16]
        if time.startswith("0"):
            time1 = int(time[1])
            time2 = int(time[3:5])
            if time1 < 15:
                print("test1")
                time1 = str(15 - time1)
                time2 = str(60 - time2)
            elif (time1 > 15) & (time1 < 21):
                print("test2")
                time1 = str(21 - time1)
                time2 = str(60 - time2)
            elif time1 > 21:
                print("test5")
                time1 = str(15 + (24 - time1))
                time2 = str(60 - time2)
        else:
            time1 = int(time[0:1])
            time2 = int(time[3:5])
            if time1 < 15:
                print("test3")
                time1 = str(15 - time1)
                time2 = str(60 - time2)
            elif time1 > 15:
                print("test4")
                time1 = str(21 - time1)
                time2 = str(60 - time2)
        await client.send_message(message.channel, "Current Time: \t" + time + "\n" + "Time to HQ: \t" + time1+":"+time2)
    # Changes colin's nickname
    x = message.server.members
    for member in x:
        if member.name == "PardonTheSuit":
            if message.content.startswith("<@!338503364751130627>"):
                await client.change_nickname(member, message.content[23:])
            #elif message.author == member:
            #    await client.delete_message(message)
            #    await client.send_message(message.channel, "Just me and my :two_hearts:daddy:two_hearts:, hanging out I got pretty hungry:eggplant: so I started to pout :disappointed: He asked if I was down :arrow_down:for something yummy :heart_eyes::eggplant: and I asked what and he said he'd give me his :sweat_drops:cummies!:sweat_drops: Yeah! Yeah!:two_hearts::sweat_drops: I drink them!:sweat_drops: I slurp them!:sweat_drops: I swallow them whole:sweat_drops: :heart_eyes: It makes :cupid:daddy:cupid: :blush:happy:blush: so it's my only goal... :two_hearts::sweat_drops::tired_face:Harder daddy! Harder daddy! :tired_face::sweat_drops::two_hearts: 1 cummy:sweat_drops:, 2 cummy:sweat_drops::sweat_drops:, 3 cummy:sweat_drops::sweat_drops::sweat_drops:, 4:sweat_drops::sweat_drops::sweat_drops::sweat_drops: I'm :cupid:daddy's:cupid: :crown:princess :crown:but I'm also a whore! :heart_decoration: He makes me feel squishy:heartpulse:!He makes me feel good:purple_heart:! :cupid::cupid::cupid:He makes me feel everything a little should!~ :cupid::cupid::cupid: :crown::sweat_drops::cupid:Wa-What!:cupid::sweat_drops::crown:")
    # Responds to the user with Pong!
    if message.content.upper().startswith("?PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    # Gets the status on Skyrim Together
    if message.content.upper().startswith("?RIM"):
        while True:
            try:
                url = "http://www.reddit.com/r/SkyrimTogether/comments/7hhux1/live_todo_list"
                values = {"s": "basics",
                          "submit": "search"}
                data = urllib.parse.urlencode(values)
                data = data.encode("utf-8")
                req = urllib.request.Request(url, data)
                resp = urllib.request.urlopen(req)
                respData = resp.read()
                paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
                for eachP in paragraphs:
                    if "Last update" in eachP:
                        await client.send_message(message.channel, eachP[8:len(eachP) - 9])
                break
            except:
                # await client.send_message(message.channel, "There was an error, please retry the command.")
                print("retry")
                pass
    # Has the bot message a specific user message
    if message.content.upper().startswith("?SAY"):
        await client.delete_message(message)
        #if message.author.id == "175441095210041344":
        if len(message.content) > 5:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Please enter something to say.")
        #else:
        #await client.send_message(message.channel, "You lack permission to perform the specified command.")
    # Has the bot lists all of the possible user commands
    if message.content.upper() == "?HELP":
        command_list = ["Ark - Gives steam-connect for the ark server", "HQ - Gives time until the next HQ game",
                        "Testbot - Tests to see if the bot is working", "Ping - Pong!",
                        "Say - Tells the bot to say something",
                        "Rim - Gets the date of the last Skyrim Together reddit update"]
        await client.send_message(message.channel, "All commands are preceded by a \'?\'.\n--------")
        for com in command_list:
            await client.send_message(message.channel, "-\t" + com)

client.run("secretkey")