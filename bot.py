# Made by chase
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Garbage cleaner is ready.")

@client.event
async def on_message(message):
    if message.content == "nick":
        await client.send_message(message.channel, "posts cancer")


client.run("NDA1NDE3MDI2ODk5ODA0MTY2.DUkGkA.mFjXHKhV21rwx5HlIbpfw07eub8")
