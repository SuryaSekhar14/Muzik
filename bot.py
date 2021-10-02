import discord
import time
from discord import channel
from discord.member import VoiceState
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv('.env')

CHANNEL_ID=os.getenv('CHANNEL_ID')
VOICE_ID=os.getenv('VOICE_ID')
client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    print('Bot is Ready.')
    channel = client.get_channel(CHANNEL_ID)
    print(channel)
    await channel.send("Muzik Alive")

#FUNCTIONS
@client.command()            #Check bot's Latency
async def ping(ctx):
    await ctx.send(f'What do you expect, Pong?\nLatency= {round(client.latency*1000)}ms')
    print(ctx.author)

@client.command(pass_context=True)        #Join Voice Channel
async def join(ctx):
    #vcchannel=client.get_channel(VOICE_ID)
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Joined!")

@client.command(pass_context=True)        #leave Voice Channel
async def leave(ctx):
    try:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the Meeting")
    except:
        await ctx.send("I am not in the Meeting.")

client.run(os.getnev('TOKEN'))
