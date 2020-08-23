import discord
import logging
from discord.ext import commands
import random
import asyncio
import os

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as {0.user}!'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower().startswith('congrat'):
        for i in range(0,2):
            await message.channel.send(':confetti_ball::confetti_ball::confetti_ball:\nCONGRATULATIONS!!!')
    
    if message.channel.name == 'arma-discussion':
        counter = random.randint(1,100)
        if counter < 3:
            await message.channel.send('USAF is watching.')

    try:
        await bot.process_commands(message) #this is required or the bot will be stuck in the on_message and not see the commands
    except:
        return

@bot.command()
async def load(ctx, extension):
    await my_load(ctx, extension, bot)

@bot.command()
async def unload(ctx, extension):
    await my_unload(ctx, extension, bot)

@bot.command()
async def reload(ctx, extension):
    await my_unload(ctx, extension, bot)
    await my_load(ctx, extension, bot)

async def my_load(ctx, extension, bot):
    try:
        bot.load_extension('cogs.{0}'.format(extension))
        await ctx.channel.send('Extension \'{0}\' loaded!'.format(extension))
    except:
        await ctx.channel.send('Load \'{0}\' failed!'.format(extension))

async def my_unload(ctx, extension, bot):
    try:
        bot.unload_extension('cogs.{0}'.format(extension))
        await ctx.channel.send('Extension \'{0}\' unloaded!'.format(extension))
    except:
        await ctx.channel.send('Unload \'{0}\' failed!'.format(extension))


print('working directory is {0}'.format(os.getcwd()))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            loadThis = filename[:-3]
            bot.load_extension('cogs.{0}'.format(loadThis))
            print('cog ' + filename + ' loaded.')
        except:
            print('cog ' + filename + ' failed!')

#For use when running from a real filesystem

##with open(r'./baby-bot-token.txt', 'r') as f:
##    token = f.read()
##bot.run(token)

#For use when deployed via heroku (using config vars to feed in the token)

bot.run(process.env.token)



