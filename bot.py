import discord
import time
from discord import channel
from discord.member import VoiceState
from discord.ext import commands

TOKEN='ODgyMzIyMzk1MTQ5NTI1MDMz.YS5sww.3gMbMcuKomRiPGg9HS-PqMn_AaY'
CHANNEL_ID='882323144315138098'
VOICE_ID='882325041189126155'
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
    vcchannel=client.get_channel(VOICE_ID)
    await vcchannel.connect()
    await ctx.send("Joined!")

@client.command(pass_context=True)        #leave Voice Channel
async def leave(ctx):
    try:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the Meeting")
    except:
        await ctx.send("I am not in the Meeting.")

client.run(TOKEN) 