import discord, googletrans, os
from googletrans import Translator
translator = Translator()
from discord.ext import commands
token = os.environ.get('BOT_TOKEN')
#=====Translate==============================
def translate(text,languarge):
  result = translator.translate(text, dest=languarge)
  return result
#================================

Bot = commands.Bot(command_prefix='no prefix!!!')
Bot.remove_command('help')

@Bot.event
async def on_ready():
  print(f'[SYS] {Bot.user} online!')
  await Bot.change_presence(activity= discord.Game(name= f'{Bot.user.name} by Blockman_#0431!'))

@Bot.event
async def on_message(message):
  if (not message.author == Bot.user):
    w = await message.channel.create_webhook(name=message.author.name)
    await w.send(f'**EN:** {translate(message.content, "en").text}\n========================\n**RU:** {translate(message.content,"ru").text}', avatar_url= message.author.avatar_url)
    await w.delete()
    await message.delete()
  
Bot.run(str(token))
