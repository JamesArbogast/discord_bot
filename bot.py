import os
import discord
import pyperclip

my_secret = os.environ['bot']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel) == "general" and message.content.startswith('/'):
        await message.channel.purge(limit=1)
        if message.content.startswith('/html'):
            content = message.content.replace('/html', '')
            nl = '\n'
            await message.channel.send(f'```html{nl}{content}{nl}```')
            print("This is working HTML")
        if message.content.startswith('/py'):
            content = message.content.replace('/py', '')
            nl = '\n'
            await message.channel.send(f'```py{nl}{content}{nl}```')
            print("This is working for python")
        if message.content.startswith('/js'):
            content = message.content.replace('/js', '')
            nl = '\n'
            await message.channel.send(f'```js{nl}{content}{nl}```')
            print("This is working for JS")