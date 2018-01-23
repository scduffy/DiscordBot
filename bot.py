import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="!")

# Print on startup to verify that bot is running locally.
@client.event
async def on_ready():
    print("Garbage cleaner is ready.")


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

# Scans all messages posted on server.
@client.event
async def on_message(message):
    message_length = 200
    # If someone posts just nick in lowercase the bot will respond with "posts cancer".
    if message.content == "nick":
        await client.send_message(message.channel, "posts cancer")

    elif message.content.startswith('!memeify'):
        args = message.content.split(" ")
        to_meme = ""
        for word in args[1:]:
            to_meme = to_meme + word

        memed_string = memeify(to_meme)
        await client.send_message(message.channel, memed_string)

    # Checks the author of the post is nick.
    elif message.author.id == "344194195344588810":
        # Checks if the length of the message exceeds 200 characters (can be changed later to less).
        if len(message.content) >= message_length:
            # Deletes message and notifies server of deletion.
            await client.delete_message(message)
            await client.send_message(message.channel, "Message has been auto-deleted due to the detection of excess autism.")

client.run("NDA1NDE3MDI2ODk5ODA0MTY2.DUkGkA.mFjXHKhV21rwx5HlIbpfw07eub8")
