import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime
import os


# client bot thing
bot = commands.Bot(command_prefix = "!",intents = discord.Intents.all())
bot.remove_command("help")

# print(datetime.datetime.today().day)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.get_channel(818021991247511574).send('**~ Look bby, iπ did a thing π ~**\n type **!help** for commands!')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def help(ctx):
    await ctx.send('***here lies the anniversary bot commands!***π\n\n'
                    '**!help** -- prints bot commands π€\n'
                    '**!date** -- tells what date our anniversary is π\n'
                    '**!today** -- tells whether today is our anniversary or not β\n'
                    '**!together** -- tells how long we\'ve been together βΎοΈ\n'
                    '**!next** -- tells how long till next anniversary β\n'
                    '**!kill** -- kills da bot π€π«\n')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def date(ctx):
    await ctx.send('date of anniversary: **November 20th, 2019**π')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def together(ctx):
    x = datetime.today() - datetime(2019, 11, 20)
    days = x.days
    seconds = x.seconds

    year = days // 365
    days = days - (365* year)
    month = days // 30
    days = days - (30 * month)
    hours = seconds // 3600
    seconds = seconds - (3600 * hours)
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)
    await ctx.send('*~you two π₯§ **cutie pies** π₯§ have been together for...~*')
    await ctx.send('***' + str(year) + '*** years, ***' + str(month) + '*** months, ***' + str(days) + '*** days, ***' + str(hours) + '*** hours, ***' + str(minutes) + '*** minutes, ***' + str(seconds) + '*** seconds '+'π±')


@bot.command()
async def next(ctx):

    x = datetime.today()
    if x.month == 12:
        if x.day >= 20:
            y = datetime(year=x.year+1,month=1,day=20)
        else:
            y = datetime(year=x.year,month=x.month,day=20)
    else:
        if x.day >= 20:
            y = datetime(year=x.year,month=x.month+1,day=20)
        else:
            y = datetime(year=x.year,month=x.month,day=20)
    z = y-x
    days = z.days
    seconds = z.seconds
    hours = seconds // 3600
    seconds = seconds - (3600 * hours)
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)
    await ctx.send('*~get hyyppeeddπ―, your next anniversary is in...~*')
    await ctx.send('β±οΈ ***'+ str(days) + '*** days, ***' + str(hours) + '*** hours, ***' + str(minutes) + '*** minutes, ***' + str(seconds) + '*** seconds ')

@bot.command()
async def today(ctx):
    if datetime.today().day != 20:
        await ctx.send('**no, its not today** π’')
    else:
        await ctx.send('**yea it is! YAYAY! don\'t forget to give kithes** π')

# Kill_Bot command: ends the game that is currently gonig onskips the timer for lobby creation
@bot.command()
async def kill(ctx):
    await ctx.send('bye love birds π₯ππ₯')
    await ctx.send('i die now β°οΈ')
    await bot.logout()

#bot token
bot.run(os.environ['token'])



