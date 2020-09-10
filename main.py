import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot

json_data = open('private.json')
data = json.load(json_data)

client: Bot = commands.Bot(command_prefix='qt ')
client.remove_command('help')
owner = ["319718067066109967"]

client.load_extension('cogs.hypixelapi')
client.load_extension('cogs.admin')
client.load_extension('cogs.misc')
client.load_extension('cogs.fun')
client.load_extension('cogs.own')


client.run(data["discordKey"])
json_data.close()

