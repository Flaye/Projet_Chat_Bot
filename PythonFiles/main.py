import discord
import os
from dotenv import load_dotenv
#import keep_alive as kpa
import nlp
import data_import

#print(data_import.geoplaces2)

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = {id:os.getenv('DISCORD_ID_GUILD')}

client = discord.Client()

print(data_import.geoplaces2.head(10))

@client.event
async def on_ready():
  #guild = discord.utils.get(client.guilds, id=GUILD)
  #for guild in, client.guilds:
  #  if guild.id == GUILD:
  #    break
  #print(f'{guild.name}', f' {guild.id} id Discord')
  print(f'{client.user} has connected to Discord')

#First message
hello=['hi','hello','heyo','chatbot']

@client.event
async def on_message(message):
  # Checking if the author is bot
  if not message.author.bot:
    # ==== Launch Chat Bot with Hi ====
    if message.content.lower() in hello:
        msg = "Hi ! Welcome to the chatBot of Where could I eat ?\nYou are looking for a restaurant ?\nJust ask : Tell me more about <The name of the restaurant>" \
              "\nYou know what you would like to eat, but you don't know where ?\nJust ask : I would like to eat <The type of food> (for example: French food !) :smiley:"
        await message.channel.send(msg)
    # ==== End Chat Bot first call ====
    elif message.content.lower() == 'test':
        await message.channel.send('This is a test message')
    else:
        rep = nlp.NLP(message.content)
        for v in rep:
            if(v['txt'] != ''):
              await message.channel.send(v['txt'])
            if(v['link'] != None):
              await message.channel.send(v['link'])

#kpa.keep_alive()
client.run(TOKEN)
