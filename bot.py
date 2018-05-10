import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from datetime import datetime
import random
import pytz


Client = discord.Client()
client = commands.Bot(command_prefix="!")


# Print on startup to verify that bot is running locally.
@client.event
async def on_ready():
    print("Garbage cleaner is ready.")


def get_timestamp():
    full_time = str(datetime.now()).split(" ")
    time = full_time[1].split(".")
    full_time[1] = time[0]

    date = full_time[0].split("-")

    timestamp = str(date[1] + "/" + date[2] + "/" + date[0] + " @ " + full_time[1] + "(EST)")

    return timestamp


def mick_time():
    utc_time = datetime.utcnow()
    time_zone = pytz.timezone("Europe/London")

    time = str(pytz.utc.localize(utc_time, is_dst=None).astimezone(time_zone))

    date, current_time = time.split(" ")
    current_time = current_time.split(".")
    current_time = current_time[0]

    cleaned_time = "__**Current Mick Time:**__\n" + current_time + "\n\n__**Current Mick Date:**__\n" + date

    return cleaned_time


def cn_insult():
    insult = "__**Chinese Insult:**__\n"
    file = open("cn_insults.txt", encoding="utf8")
    insult_list = []

    for line in file:
        insult_list.append(line)

    insult_index = random.randint(0, len(insult_list)-1)
    insult += insult_list[insult_index]

    return insult


def time_to_hq():
    full_time = str(datetime.now()).split(" ")

    new_seconds = full_time[1].split(".")
    full_time[1] = new_seconds[0]

    clean_time = full_time[1].split(":")

    FMT = "%H:%M:%S"
    first_hq_time = "15:00:00"
    second_hq_time = "21:00:00"

    OUTPUT_STRING = "__**Current Time:**__\n" + full_time[1] + "\n"

    if int(clean_time[0]) < 15:
        time_left = datetime.strptime(first_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        OUTPUT_STRING += ("\n__**Next HQ Time:**__\n15:00:00\n\n__**Time remaining to HQ:**__ \n" + out_time[0] + " Hour(s) " + out_time[1]
                          + " Minute(s) " + out_time[2] + " Second(s)")

    elif int(clean_time[0]) < 21 and int(clean_time[0]) >= 15:
        time_left = datetime.strptime(second_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        OUTPUT_STRING += ("\n__**Next HQ Time:**__\n21:00:00\n\n__**Time remaining to HQ:**__ \n" + out_time[0] + " Hour(s) "
                          + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)")

    else:
        time_left = datetime.strptime(first_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")
        fixed_hour = out_time[0].split(",")

        OUTPUT_STRING += ("\n__**Next HQ Time:**__\n15:00:00\n\n__**Time remaining to HQ:**__ \n" + fixed_hour[1] + " Hour(s) "
                          + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)")

    return OUTPUT_STRING


def caps(string):
    memed_string = ""
    string = string.lower()
    string = string.strip()
    for i in range(len(string)):
        if i % 2 == 0:
            if string[i] == " " or string[i] == "?" or string[i] == "!" or string[i] == "." or string[i] == "\"" or string[i] == "," or string[i] == "'" or string[i] == "’" or string[i] == ":" or string[i] == ";" or string[i] == "-":
                memed_string = "  " + memed_string + " "
            else:
                memed_string = memed_string + string[i].upper()
        else: memed_string = memed_string + string[i]

    return memed_string


def retrieve_nickpost():
    output = "__**Retrieved Random Archived Nickpost:**__\n"
    file = open("nickposts.txt")
    nickpost_list = []


    for nickpost in file:
        nickpost.replace("“", "\"")
        nickpost.replace("@", "\"")
        nickpost_list.append(nickpost)


    nickpost_index = random.randint(0, len(nickpost_list)-1)
    output += nickpost_list[nickpost_index]

    nickpost_list.clear()

    return output


def save_nickpost(message):
    nickpost_list = []
    read_file = open("nickposts.txt", "r")
    for nickpost in read_file:
        nickpost = nickpost.replace("[]\"", "")
        #nickpost = nickpost.replace("]", "")
        nickpost_list.append(nickpost)
    read_file.close()

    clear_file = open("nickposts.txt", "w")
    clear_file.write("")
    clear_file.close()

    temp_file = open("tempfile.txt", "w")
    temp_file.write(message)
    temp_file.close()

    new_message = ""
    temp_file = open("tempfile.txt", "r")
    for line in temp_file:
        line = line.replace("@", "")
        line = line.replace("\n", "")
        new_message += line
        #new_message += line.replace("\n", "")

    temp_file.close()

    temp_file = open("tempfile.txt", "w")
    temp_file.write("")
    temp_file.close()

    with open("nickposts.txt", "a") as file:
        nickpost_list.append(get_timestamp() + ":" + "\n" + new_message)
        #in_message = message.strip()
        for chromosome in nickpost_list:
            chromosome = chromosome.replace("[]", "")
            chromosome = chromosome.replace("\n", "")

            chromosome = chromosome.replace("@", "")

            file.write(chromosome + "\n")
            #file.write(str(nickpost_list))
    nickpost_list.clear()
    file.close()


# Aiden memeify function
def memeify(string):
    memed_string = ""
    string = string.lower()
    string = string.strip()
    for i in range(len(string)):
        if string[i] == " " or string[i] == "?" or string[i] == "!" or string[i] == "." or string[i] == "\"" or string[i] == "," or string[i] == "'" or string[i] == "’" or string[i] == ":" or string[i] == ";" or string[i] == "-":
            memed_string = " " + memed_string
        elif string[i] == "b":
            memed_string = memed_string + " :b:"
        else:
            memed_string = memed_string + " :regional_indicator_" + string[i] + ":"
    return memed_string


def to_piglatin(message):
    output = ""
    consonant_pairs = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    vowls = ['a', 'e', 'i', 'o', 'u']
    message = message.split()
    for word in message:
        if word[:2] in consonant_pairs:
            output += word[2:] + word[:2] + "ay "
        elif not word[0] in vowls:
            output += word[1:] + word[0] + "ay "
        else:
            output += word + "way "

    return output


# Scans all messages posted on server.
@client.event
async def on_message(message):
    message_length = 200
    # If someone posts just nick in lowercase the bot will respond with "posts cancer".
    if message.content.upper() == "NICK":
        await client.send_message(message.channel, "What do you do?")

    elif message.content.upper() == "!NICKPOST":
        await client.send_message(message.channel, retrieve_nickpost())

    elif message.content.upper() == "!MICK":
        await client.send_message(message.channel, mick_time())

    elif message.content.upper() == "!CN":
        await client.send_message(message.channel, cn_insult())

    elif message.content.upper() == "!HQ":
        await client.send_message(message.channel, time_to_hq())

    elif message.content.upper() == "COLIN" or message.content.upper() == "JACK":
        await client.send_message(message.channel, "is a THOT. ")

    elif message.content.upper() == "RYAN":
        await client.send_message(message.channel, "knows his root beer. ")

    elif message.content.upper() == "JOON":
        await client.send_message(message.channel, "is a clear toaster boi.")

    elif message.content.upper() == "CHASE" or message.content.upper() == "AIDEN" or message.content.upper() == "NEIL":
        await client.send_message(message.channel, "is a CHAD.")

    elif message.content.startswith('!begone'):
        #nick_id = discord.Server.get_member(discord.Server._members, "88489537772212224")
        #colin_id = discord.Server.get_member(discord.Server._members, "349714851926507523")
        await client.send_message(message.channel, "Begone THOT!")
        #await client.kick(colin_id)

        # await client.move_member(nick_id, client.get_channel("382960361860497428"))

    elif message.content.upper() == "DO U KNO DE WAE":
        await client.send_message(message.channel, "http://i0.kym-cdn.com/photos/images/original/001/330/335/b84.png")
        await client.send_message(message.channel, "I kno de wae my brotha.")

    elif message.content.upper() == "!WELCOME":
        await client.send_message(message.channel, "Welcome to Nick's Autism Pit!")

    elif message.content.upper() == "!TEST":
        #await client.delete_message(message)
        await client.send_message(message.channel, "https://media.tenor.com/images/2063f80cb02309fd6a3c4da500a1d1de/tenor.gif")
        await client.send_message(message.channel, "CONCERN")

    # Makes capitals out of the given string.
    elif message.content.startswith('!caps'):
        args = message.content.split(" ")
        to_meme = ""
        #await client.delete_message(message)
        for word in args[1:]:
            to_meme = to_meme + word

        memed_string = caps(to_meme)
        await client.send_message(message.channel, memed_string)

    # Bolds the string given.
    elif message.content.startswith('!memeify'):
        args = message.content.split(" ")
        to_meme = ""
        #await client.delete_message(message)
        for word in args[1:]:
            to_meme = to_meme + word

        memed_string = memeify(to_meme)
        await client.send_message(message.channel, memed_string)

    elif message.content.startswith('!pig'):
        args = message.content.split(" ")
        to_meme = ""
        for word in args[1:]:
            to_meme = to_meme + word + " "

        memed_string = to_piglatin(to_meme)
        await client.send_message(message.channel, memed_string)

    # Checks the author of the post is nick.
    #nick id = 344194195344588810
    #chase id = 212286463642042369
    elif message.author.id == "344194195344588810":
        # Checks if the length of the message exceeds 200 characters (can be changed later to less).
        if len(message.content) >= 200:
            save_nickpost(message.content)
            await client.send_message(message.channel, "*AUTISM DETECTED: ARCHIVING NICKPOST*")
            # the_id = '<@344194195344588810>'
            # # Deletes message and notifies server of deletion.
            # print(message)
            # #await client.delete_message(message)
            # # await client.send_message(message.channel, ' : %s is the best ' % myid)
            # #await client.send_message(message.channel, "A message from %s has been auto-deleted due to the detection of excess autism." % the_id)

    elif message.content.startswith('!testbot'):
        await client.send_message(message.channel, "Responding.")

auth_file = open("auth.txt")
auth_key = ""
for line in auth_file:
    auth_key = line

client.run(auth_key)
