import discord
import os
import random
from keep_alive import keep_alive
from dice import dice
import re
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
  if re.match('\dD\d\d\d',message.content) or re.match('\dD\d\d',message.content) or re.match('\dD\d',message.content):
    await message.channel.send(dice(message))
keep_alive()
client.run(os.getenv('TOKEN'))
#TOKEN is enviroment variable