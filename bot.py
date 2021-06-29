# bot.py
import os

import discord

TOKEN = 'ODU5MjAzNjU0Mzc2NzUxMTM2.YNpRwg.LGunq2GxFzItIf-SSLqGyYI-EqA'
print(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)