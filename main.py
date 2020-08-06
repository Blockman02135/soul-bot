import discord, googletrans, os
from googletrans import Translator
translator = Translator()
from discord.ext import commands
token = os.environ.get('BOT_TOKEN')
#=====Translate==============================
def translate(text,languarge):
  result = translator.translate(text, dest=languarge)
  return result
#============================================
Bot = commands.Bot(command_prefix='no prefix!!!')
Bot.remove_command('help')

@Bot.event
async def on_ready():
  print(f'[SYS] {Bot.user} online!')
  await Bot.change_presence(activity= discord.Game(name= f'{Bot.user.name} by Blockman_#0431!'))

@Bot.event
async def on_message(message):
  if (not message.author.discriminator=="0000" and not message.author==Bot.user):
    smsg =f'**EN:** {translate(message.content, "en").text}\n========================\n**RU:** {translate(message.content,"ru").text}'
    logmsg = discord.Embed(
      title= f'**{message.author}** sended message',
      color=0xfff000,
      timestamp=message.created_at)
    logmsg.description=(
      f'Message has been sended in channel {message.channel.mention}'
    )
    logmsg.add_field(
        name= 'Message',
        value= message.content
    )
    logmsg.add_field(
        name= 'EN',
        value= translate(message.content, "en").text
    )
    logmsg.add_field(
        name= 'RU',
        value= translate(message.content, "ru").text
    )
    logmsg.set_thumbnail(url=message.author.avatar_url)
    logmsg.set_footer(text=f'Message languarge: {translate(message.content, "en").src}')
    log_C = Bot.get_channel(740908170679156737)
    await log_C.send(embed=logmsg)
    w = await message.channel.create_webhook(name=message.author.name)
    await w.send(smsg, avatar_url= message.author.avatar_url)
    await w.delete()
    await message.delete()
  
Bot.run(str(token))
