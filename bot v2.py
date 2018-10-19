import discord
from discord.ext import commands
from datetime import datetime
import random
from discord import Game
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='!')
afk_set = {}


# All helper functions
def time_to_hq():
    full_time = str(datetime.now()).split(" ")

    new_seconds = full_time[1].split(".")
    full_time[1] = new_seconds[0]

    clean_time = full_time[1].split(":")

    FMT = "%H:%M:%S"
    first_hq_time = "15:00:00"
    second_hq_time = "21:00:00"

    embed = discord.Embed(title="Time to HQ", description="Countdown to the next HQ stream.", color=0xeee657)
    embed.add_field(name="Current Time", value=full_time[1])

    if int(clean_time[0]) < 15:
        time_left = datetime.strptime(first_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        embed.add_field(name="Next HQ Time", value="15:00:00")
        embed.add_field(name="Time Remaining to HQ",
                        value=(out_time[0] + " Hour(s) " + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)"))

    elif int(clean_time[0]) < 21 and int(clean_time[0]) >= 15:
        time_left = datetime.strptime(second_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")

        embed.add_field(name="Next HQ Time", value="21:00:00")
        embed.add_field(name="Time Remaining to HQ",
                        value=(out_time[0] + " Hour(s) " + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)"))

    else:
        time_left = datetime.strptime(first_hq_time, FMT) - datetime.strptime(full_time[1], FMT)
        out_time = str(time_left).split(":")
        fixed_hour = out_time[0].split(",")

        embed.add_field(name="Next HQ Time", value="15:00:00")
        embed.add_field(name="Time Remaining to HQ",
                        value=(fixed_hour[1] + " Hour(s) " + out_time[1] + " Minute(s) " + out_time[2] + " Second(s)"))

    return embed


def cn_insult():
    embed = discord.Embed(title="CN Insult", description="Random Chinese Insult.", color=0xeee657)

    file = open("cn_insults.txt", encoding="utf8")
    insult_list = []

    for line in file:
        insult_list.append(line)

    insult_index = random.randint(0, len(insult_list)-1)
    #insult += insult_list[insult_index]
    embed.add_field(name="Insult", value=insult_list[insult_index])

    return embed


def to_caps(string):
    memed_string = ""
    string = string.lower()
    string = string.strip()
    for i in range(len(string)):
        if i % 2 == 0:
            if string[i] == " " or string[i] == "?" or string[i] == "!" or string[i] == "." or string[i] == "\"" or string[i] == "," or string[i] == "'" or string[i] == "’" or string[i] == ":" or string[i] == ";" or string[i] == "-":
                memed_string = "  " + memed_string + " "
            else:
                memed_string = memed_string + string[i].upper()
        else:
            memed_string = memed_string + string[i]

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


def to_memeify(string):
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


def get_timestamp():
    full_time = str(datetime.now()).split(" ")
    time = full_time[1].split(".")
    full_time[1] = time[0]

    date = full_time[0].split("-")

    timestamp = str(date[1] + "/" + date[2] + "/" + date[0] + " @ " + full_time[1] + "(EST)")

    return timestamp


def save_nickpost(message):
    nickpost_list = []
    read_file = open("nickposts.txt", "r")
    for nickpost in read_file:
        nickpost = nickpost.replace("[]\"", "")
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

    temp_file.close()

    temp_file = open("tempfile.txt", "w")
    temp_file.write("")
    temp_file.close()

    with open("nickposts.txt", "a") as file:
        nickpost_list.append(get_timestamp() + ":" + "\n" + new_message)
        for chromosome in nickpost_list:
            chromosome = chromosome.replace("[]", "")
            chromosome = chromosome.replace("\n", "")

            chromosome = chromosome.replace("@", "")

            file.write(chromosome + "\n")
    nickpost_list.clear()
    file.close()


def retrieve_nickpost():
    output = "__**Retrieved Random Archived Nickpost:**__\n"
    file = open("nickposts.txt")
    nickpost_list = []

    for nickpost in file:
        nickpost.replace("“", "\"")
        nickpost.replace("@", "__at__")
        nickpost_list.append(nickpost)

    nickpost_index = random.randint(0, len(nickpost_list)-1)
    output += nickpost_list[nickpost_index]

    nickpost_list.clear()

    return output


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('- - - - - -')
    await bot.change_presence(activity=Game(name="Programming: The Andres/Colin Odyssey"))


@bot.event
async def on_message(message):
    if message.author.id == 344194195344588810:
        if len(message.content) >= 200:
            save_nickpost(message.content)
            await message.channel.send("*AUTISM DETECTED: ARCHIVING NICKPOST*")

    mentions = message.mentions

    for mention in mentions:
        if str(mention) in afk_set:
            await message.channel.send(str(mention)[:-5] + " is currently AFK and cannot respond.")

    if str(message.author) in afk_set:
        if message.content != "!afk":
            if message.content == "!bak":
                await message.channel.send(str(message.author) + " is no longer AFK.")
                del afk_set[str(message.author)]

    await bot.process_commands(message)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Autism Removal", description="A bot that deals with dank memes.", color=0xeee657)
    embed.add_field(name="Author", value="<ExtremisVis#3182>")
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="[Invite Link](<https://discordapp.com/api/oauth2/authorize?client_id=405417026899804166&permissions=8&scope=bot>)")
    await ctx.send(embed=embed)


@bot.command()
async def testbot(ctx):
    await ctx.send("Responding.")


@bot.command()
async def andres(ctx):
    await ctx.send('https://www.sololearn.com/')


@bot.command()
async def music(ctx):
    await ctx.send(".play https://www.youtube.com/watch?v=FTQbiNvZqaY")
    await ctx.send(".play https://www.youtube.com/watch?v=djV11Xbc914")
    await ctx.send(".play https://www.youtube.com/watch?v=izGwDsrQ1eQ")
    await ctx.send(".play https://www.youtube.com/watch?v=YkADj0TPrJA")


@bot.command()
async def change_status(ctx, *, message: str):
    if str(ctx.message.author) == "ExtremisVis#3182":
        await bot.change_presence(activity=Game(name=message))
    else:
        await ctx.send("You do not have the required permissions to preform this command.")


@bot.command(pass_context=True)
async def afk(ctx):
    user = str(ctx.message.author)
    if user in afk_set:
        await ctx.send(user[:-5] + " you are already AFK you idiot.")
    else:
        await ctx.send(user[:-5] + " is now AFK.")
        afk_set[user] = get_timestamp()


@bot.command(pass_context=True)
async def bak(ctx):
    user = str(ctx.message.author)
    if user in afk_set:
        del afk_set[user]
        await ctx.send(user[:-5] + " is no longer AFK.")
    # else:
    #     await ctx.send(user[:-5] + " you are not AFK you idiot.")


@bot.command()
async def afks(ctx):
    embed = discord.Embed(title="AFKs", description="All of the current AFK users and the time they went AFK.", color=0xeee657)
    for afk_user in afk_set:
        embed.add_field(name=afk_user, value=afk_set[afk_user], inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def nickpost(ctx):
    await ctx.send(retrieve_nickpost())


@bot.command()
async def post(ctx):
    await ctx.send("Nickpost File:", file=discord.File('nickposts.txt'))


@bot.command()
async def memeify(ctx, *, message: str):
    args = message.split(" ")
    to_meme = ""
    # await client.delete_message(message)
    for word in args:
        to_meme = to_meme + word + " "

    memed_string = to_memeify(to_meme)
    await ctx.send(memed_string)


@bot.command()
async def pig(ctx, *, message: str):
    args = message.split(" ")
    to_meme = ""
    for word in args:
        to_meme = to_meme + word + " "

    memed_string = to_piglatin(to_meme)
    await ctx.send(memed_string)


@bot.command()
async def caps(ctx, *, message: str):
    args = message.split(" ")
    to_meme = ""
    # await client.delete_message(message)
    for word in args:
        to_meme = to_meme + word

    memed_string = to_caps(to_meme)
    await ctx.send(memed_string)


@bot.command()
async def hq(ctx):
    await ctx.send(embed=time_to_hq())


@bot.command()
async def cn(ctx):
    await ctx.send(embed=cn_insult())


@bot.command()
async def nick(ctx):
    import random
    random_num = random.randint(0, 11)

    if random_num == 0:
        await ctx.send('https://imgur.com/cGFowTm')
    elif random_num == 1:
        await ctx.send('https://imgur.com/R5Zauh1')
    elif random_num == 2:
        await ctx.send('https://imgur.com/fb8Ycvp')
    elif random_num == 3:
        await ctx.send('https://imgur.com/zNqA4gw')
    elif random_num == 4:
        await ctx.send('https://imgur.com/a98oORn')
    elif random_num == 5:
        await ctx.send('https://imgur.com/lmZFABR')
    elif random_num == 6:
        await ctx.send('https://imgur.com/wfT7PKt')
    elif random_num == 7:
        await ctx.send('https://imgur.com/CQi6CuS')
    elif random_num == 8:
        await ctx.send('https://imgur.com/mn4g8Dc')
    elif random_num == 9:
        await ctx.send('https://imgur.com/PDDKdJM')
    elif random_num == 10:
        await ctx.send('https://imgur.com/vPFFoip')
    elif random_num == 11:
        await ctx.send('https://imgur.com/3fsoArI')

bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Autism Removal", description="A bot that deals with dank memes. List of commands are:", color=0xeee657)

    embed.add_field(name="!info", value="Gives some statistics about the bot", inline=False)
    embed.add_field(name="!nick", value="Gets a random image of nik from imgur.", inline=False)
    embed.add_field(name="!hq", value="Gets the time to the next HQ stream.", inline=False)
    embed.add_field(name="!cn", value="Gets a random chinese insult.", inline=False)
    embed.add_field(name="!caps", value="Returns the given input as capitalized memed version of itself.", inline=False)
    embed.add_field(name="!pig", value="Turns a given english string to piglatin.", inline=False)
    embed.add_field(name="!memeify", value="Memeifies a given string.", inline=False)
    embed.add_field(name="!post", value="Sends the current nickpost archive file to the text channel.")
    embed.add_field(name="!nickpost", value="Sends a random nickpost from the archive.")
    embed.add_field(name="!afk", value="Puts the sender into an AFK status where if mentioned, "
                                       "the bot will notify the server of AFK status.", inline=False)
    embed.add_field(name="!bak", value="Removes the users AFK status.", inline=False)
    embed.add_field(name="!afks", value="Shows an embeded list of currently AFK users.", inline=False)
    embed.add_field(name="!change_status", value="Changes the game the bot is playing to the input."
                                                 " Requires Admin permissions.", inline=False)
    embed.add_field(name="!andres", value="Reminds andres of a good place to learn how to code.", inline=False)

    await ctx.send(embed=embed)

auth_file = open("auth.txt")
auth_key = ""
for line in auth_file:
    auth_key = line

bot.run(auth_key)
