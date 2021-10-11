import os
import discord
# Replace "TOKEN" with your discord bot token
my_secret="TOKEN"
client = discord.Client()
@client.event
async def on_read():
  print("Bot logged in as{0.user}".format(client))
@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if msg.content.startswith('!link'):
    await msg.channel.send("https://meet.google.com/fxk-vdiv-tcu")#on asking for link it will send a valid pre-stored link for the meet
  elif msg.content.startswith('!bye'):
    await msg.channel.send("Bye ,have a nice day")
  elif msg.content.startswith('!goodnight'):
    await msg.channel.send("goodnight, sweet dreams")
client.run(my_secret)

