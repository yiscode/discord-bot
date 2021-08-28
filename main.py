import discord
import os
import random
from keep_alive import keep_alive
from dice import dice
from dice import change_message as cv
from dice import dice_level as dv
from dice import dice_tarot as dt
from dice import dice_person as dp
import re
client = discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  message.content = message.content.upper()
  if message.author == client.user:
    return
  if re.search(r'(\d+D\d+)',message.content):
    await message.channel.send(content=cv(message.content))
  if re.match('1DLV',message.content):
    
    await message.channel.send(dv(message))
  if re.match('1DTA',message.content):
    
    await message.channel.send(dt(message))
  if re.match('1DPE',message.content):
    
    await message.channel.send(dp(message))
keep_alive()
client.run(os.getenv('TOKEN'))
#TOKEN is enviroment variable