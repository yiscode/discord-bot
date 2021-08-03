import discord
import os
import random
from keep_alive import keep_alive
client = discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('hello'):
    await message.channel.send('hello!!!!')
  if message.content.startswith('1D10'):
    a=random.randint(1,10)
    await message.channel.send(a)
keep_alive()
client.run(os.getenv('TOKEN'))
#TOKEN is enviroment variable