# bot.py
import os
import random
import json
import asyncio
import datetime
import threading
import schedule

import discord
from discord import Member, Guild, Intents, Message
from dotenv import load_dotenv
from discord.ext import commands, timers, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

os.chdir(r'/Users/m.golden/PycharmProjects/haroBOT')

bot = commands.Bot(command_prefix='haro! ')
bot.timer_manager = timers.TimerManager(bot)
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
member = discord.Member
guild = discord.Guild
message = discord.Message

ace = '310314640921853952'
dal = '275830722831319040'
dray = '194999847223296000'
jess = '237081633604370432'
lex = '378738698927210496'
luna = '197133313633288193'
may = '222378331343945728'
mica = '197844045219758080'
neon = '575880455757365302'
panther = '364955686913966080'
purin = '343197836978159616'
xc = '404828914406522881'


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    reminders.start()
    atp_reminders.start()


# @client.event
# async def on_member_join(member):
#     with open('users.json', 'r') as f:
#         users = json.load(f)
#
#     await update_data(users, member)
#
#     with open('users.json', 'w') as f:
#         json.dump(users, f)
#
#
# @client.event
# async def on_message(message):
#     with open('users.json', 'r') as f:
#         users = json.load(f)
#
#     await update_data(users, message.author)
#
#     with open('users.json', 'w') as f:
#         json.dump(users, f)
#
# async def update_data(users, user):
#     if not user.id in users:
#         users[user.id] = {}
#        # users[user.id]['experience'] = 0
#        # users[user.id]['level'] = 1
#
# async def add_experience(users, user, exp):
#     users[user.id]['experience'] +=exp
#
# async def level_up(users, user, channel):
#     experience = users[user.id]['experience']
#     lvl_start = users[user.id]['level']
#     lvl_end = int(experience ** (1/4))
#
#     if lvl_start < lvl_end:
#         await client.send_message(channel, f'{user.mention} has leveled to level {lvl_end}')
#         users[user.id]['level'] = lvl_end

@bot.command(name='haro' or 'Haro', help='Haro Callback!', pass_context=True)
async def haro_call_back(message):
    haro_responses = ['Geese! Danger! Geese! Danger!',
                      'Augur not friend. Augur not friend. Haro...'
                      'Haro! Haro!',
                      'Haro!',
                      'Catch me! Haro!',
                      'Haro is fine! Haro is fine!',
                      f'Hello! Hello! Haro is here! Haro is here!', ]

    response = random.choice(haro_responses)
    await message.channel.send(response)


@bot.command(name='lockon' or 'Lockon', help='Lockon is here!')
async def lockon_call_back(ctx):
    lockon_responses = [
        'Lockon! Lockon!',
        'Where? Where? Lockon? Lockon?',
        'I will help! I will help!',
        'Lockon, Friend! Haro!'
    ]

    response = random.choice(lockon_responses)
    await ctx.send(response)


@bot.command(name='pic', help='Show me a Haro!')
async def haro_gif(ctx):
    haro_gifs = [
        'haro1.gif',
        'haro2.gif',
        'haro3.gif',
        'haro4.gif',
        'haro5.gif',
        'haro6gif.gif',
        'haro7.gif',
        'haro8.gif',
        'haro9.gif'
    ]

    response = random.choice(haro_gifs)
    file = discord.File("./images/" + response, filename="image.gif")
    e = discord.Embed()
    e.set_image(url="attachment://image.gif")
    await ctx.send(file=file, embed=e)


@bot.command(name='colony', help='No dont do it!')
async def colony_gif(ctx):
    colony_gifs = [
        'colonydrop.gif',
        'colonydrop2.gif',
        'colonydrop3.gif'
    ]

    response = random.choice(colony_gifs)
    file = discord.File("./images/" + response, filename="image.gif")
    e = discord.Embed()
    e.set_image(url="attachment://image.gif")
    await ctx.send(file=file, embed=e)


@bot.command(name='slap', help='Do it like Bright Noa')
async def slap_gif(ctx):
    slap_gifs = [
        'slap1.gif',
        'slap2.gif',
        'slap3.gif',
        'slap4.gif',
        'slap5.gif',
        'slap6.gif',
        'slap7.gif',
        'slap8.gif'
    ]

    response = random.choice(slap_gifs)
    file = discord.File("./images/" + response, filename="image.gif")
    e = discord.Embed()
    e.set_image(url="attachment://image.gif")
    await ctx.send(file=file, embed=e)


@bot.command(name='ac' or 'AC' or 'Ac', help='AC Reminder!')
async def ac_reminder(ctx):
    ac_remind = 'AC Reminder! Post by the last day of the month!\n' \
                'Deadline: 11:59 PM (PST)/ 2:59 AM (EST) / 7:59 am (GMT)\n' \
                'Don\'t forget, Haro!'
    await ctx.send(ac_remind)


@bot.command(name='atp' or 'ATP' or 'Atp', help='ATP/EMP Reminder!')
async def atp_reminder(ctx):
    emp_remind = 'EMP/ATP Every 15th-16th of the Month! Haro!'
    response = emp_remind
    await ctx.send(response)


@bot.command(name='rng' or 'Rng' or 'RNG', help='Give a number, get a random number up to that number from haro')
async def random_number(ctx, arg):
    embed = discord.Embed(title="Pick this one! Pick this one!", description=(random.randint(1, int(arg))))
    await ctx.send(embed=embed)


@tasks.loop(hours=168)
async def reminders():
    game_remind = 'AC Reminder! Post by the last day of the month!\n' \
                  'Deadline: 11:59 PM (PST)/ 2:59 AM (EST) / 7:59 am (GMT)\n' \
                  'Don\'t forget, Haro!'
    channel = bot.get_channel(222469946179846146)
    await channel.send(game_remind)


@tasks.loop(hours=336)
async def atp_reminders():
    atp_remind = 'EMP/ATP Every 15th-16th of the Month! Haro!'
    channel = bot.get_channel(222469946179846146)
    await channel.send(atp_remind)


bot.run('[TOKEN CODE]')
