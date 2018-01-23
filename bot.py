import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Garbage cleaner is ready.")

@client.event
async def on_message(message):
    if message.content == "nick":
        await client.send_message(message.channel, "posts cancer")
    elif message.author.id == "344194195344588810":
        if len(message.content) >= 200:
            await client.delete_message(message)
            await client.send_message(message.channel, "Message has been auto-deleted due to the detection of excess autism.")

client.run("NDA1NDE3MDI2ODk5ODA0MTY2.DUkGkA.mFjXHKhV21rwx5HlIbpfw07eub8")
