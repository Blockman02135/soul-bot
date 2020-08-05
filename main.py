import discord, googletrans, os, apiai, json
from googletrans import Translator
translator = Translator()
from discord.ext import commands
from discord import utils
token = os.environ.get('BOT_TOKEN')
#=====Translate==============================
def translate(text,languarge):
  result = translator.translate(text, dest=languarge)
  return result

#================================
#==============Speak=====================
def speakAnswer(text):
    request = apiai.ApiAI('ec3a77cf0168468488859c8625201ee8').text_request()
    request.lang = 'en'
    request.session_id = 'SoulBot'
    request.query = translate(text,'ru')
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response=''
    response = responseJson['result']['fulfillment']['speech'] 
    if response:
        return translate(response,'en')
    else:
        return translate('Я Вас не понял!','en')
#======================================


Bot = commands.Bot(command_prefix='|')
Bot.remove_command('help')
#=================Cog Reader==============================
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        Bot.load_extension(f'cogs.{file[:-3]}')

@Bot.event
async def on_ready():
  print(f'[SYS] {Bot.user} online!')
  await Bot.change_presence(activity= discord.Game(name= f'{Bot.user.name} by Blockman_#0431 for The Soul Script Server!'))

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.mention}, **Command not found!**'),delete_after=5)
        await ctx.message.delete()
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.mention}, **The command is entered incorrectly**'),delete_after=5)
        await ctx.message.delete()

@Bot.event
async def on_message(message):
  if ctx.message.author.nick:
    nname = message.author.nick
  else:
    nname = message.author.name
  if message.author=='ɹaɹoldxaʇauɹaʇu!#2036':
    w = await message.channel.create_webhook(name= nname)
    await w.send(translate(message.content, "ru").text), avatar_url= ctx.message.author.avatar_url)
    await w.delete()
    await message.delete()
  if message.author=='Blockman_#0431':
    w = await message.channel.create_webhook(name= nname)
    await w.send(translate(message.content, "en").text), avatar_url= ctx.message.author.avatar_url)
    await w.delete()
    await message.delete()

@Bot.command()
async def code(ctx, syntaxis, *, code):
  syntaxises = ['js','py','lua','html','css','c++', 'bash', 'ini', 'c', 'k', 'apache']
  if syntaxis in syntaxises:
    if ctx.message.author.nick:
      nname = ctx.message.author.nick
    else:
      nname = ctx.message.author.name
    w = await ctx.channel.create_webhook(name= nname)
    await w.send(f'Syntax: **{syntaxis}**\n```{syntaxis}\n{code}\n```', avatar_url= ctx.message.author.avatar_url)
    await w.delete()
    await ctx.message.delete()
  else:
    await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.mention}, Could not recognize syntax!'),delete_after=5)
    await ctx.message.delete()

#def colorr(argument):
#    switcher = {
#        'GOLD': 732567102657003520,
#        'RED': 732566832531111946,
#        'GREEN': 732566911665307678,
#        'LIME': 732566951678836879,
#        'BLUE': 732566998806167552,
#        'YELLOW': 732567049670230118,
#        'ORANGE': 732567176380284949
#    }
#    return switcher.get(argument, None)

@Bot.command()
async def t(ctx, languarge, *, text):
  if ctx.message.author.nick:
     nname = ctx.message.author.nick
  else:
     nname = ctx.message.author.name
  w = await ctx.channel.create_webhook(name= nname)
  await w.send(f'{translate(text, languarge).text} ||[{translate(text, languarge).src}:{translate(text, languarge).dest}]||', avatar_url= ctx.message.author.avatar_url)
  await w.delete()
  await ctx.message.delete()


@Bot.command()
async def speak(ctx,*,msg):
  w = await ctx.channel.create_webhook(name= 'Alysa')
  await w.send(speakAnswer(msg), avatar_url= 'https://st3.depositphotos.com/8950810/17657/v/450/depositphotos_176577870-stock-illustration-cute-smiling-funny-robot-chat.jpg')
  await w.delete()

@Bot.command()
@commands.is_owner()
async def load(ctx, extension):
    Bot.load_extension(f'Modules.{extension}')
    if not commands.NotOwner:
        await ctx.send(f"Ошибка доступа! Недостаточно прав.")
    else:
        await ctx.send(f"Модуль **{extension}** успешно загружен!")

@Bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    Bot.unload_extension(f'Modules.{extension}')
    if not commands.NotOwner:
        await ctx.send(f"Ошибка доступа! Недостаточно прав.")
    else:
        await ctx.send(f"Модуль **{extension}** успешно выгружен!")


@Bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    Bot.reload_extension(f'Modules.{extension}')
    if not commands.NotOwner:
        await ctx.send(f"Ошибка доступа! Недостаточно прав.")
    else:
        await ctx.send(f"Модуль **{extension}** успешно перезагружен!")

Bot.run(str(token))
