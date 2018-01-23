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

# Scans all messages posted on server.
@client.event
async def on_message(message):
    message_length = 200
    # If someone posts just nick in lowercase the bot will respond with "posts cancer".
    if message.content == "nick":
        await client.send_message(message.channel, "posts cancer")

    elif message.content.startswith('!msg_len'):
        args = message.content.split(" ")

        if not args[1].isdigit():
            await client.sent_message(message.channel, "Argument not valid, not a digit.")
        else:
            args = int(args[1])
            await client.send_message(message.channel, "Changed Nick's max message length.")
            message_length = args

    # Checks the author of the post is nick.
    elif message.author.id == "212286463642042369":
        # Checks if the length of the message exceeds 200 characters (can be changed later to less).
        if len(message.content) >= message_length:
            # Deletes message and notifies server of deletion.
            await client.delete_message(message)
            await client.send_message(message.channel, "Message has been auto-deleted due to the detection of excess autism.")

client.run("NDA1NDE3MDI2ODk5ODA0MTY2.DUkGkA.mFjXHKhV21rwx5HlIbpfw07eub8")
