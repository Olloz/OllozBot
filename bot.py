import random
import discord
from discord.ext import commands
import aiohttp
from aiohttp import request
from discord.ext.commands import Bot
import math
client: Bot = commands.Bot(command_prefix='qt ')
client.remove_command('help')
owner = ["319718067066109967"]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.watching, name="qt help"))
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined! ')


@client.event
async def on_member_remove(member):
    print(f'{member} has left! ')


@client.command()
async def pong(ctx):
    await ctx.send(f'Ping! {round(client.latency * 1000)}ms')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command(pass_context=True)
async def randomnumber(ctx):
    await ctx.send(random.randint(1, 101))


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')


@client.command()
async def panda(ctx):
    await ctx.send('**PANDA QT**')


@client.command()
async def gummy(ctx):
    await ctx.send('**GUMMY QT**')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def whois(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a %d %B %Y %I:%M %p UTC'))

    embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
    embed.add_field(name='Top role:', value=member.top_role.mention)

    embed.add_field(name='Bot?', value=member.bot)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title="Olloz's Bot Info",
                          description="Olloz's Bot is a small bot made by Olloz!", color=0x00fffb)
    embed.add_field(name="Bot usage:", value="qt [command]", inline=False)
    embed.set_footer(text=":)")
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    helpembed = discord.Embed(title="Help Menu", description="**Prefix: 'qt'**", color=0x00fffb)
    helpembed.add_field(name="Help", value="qt help", inline=True)
    helpembed.add_field(name="Bot's Ping", value="qt ping / qt pong", inline=True)
    helpembed.add_field(name="User Info", value="qt whois [user]", inline=True)
    helpembed.add_field(name="Am I qt?", value="*Being Developed*", inline=True)
    helpembed.add_field(name="8 Ball", value="qt 8 ball [question]", inline=True)
    helpembed.add_field(name="Kick User", value="qt kick", inline=True)
    helpembed.add_field(name="Ban User", value="qt ban", inline=True)
    helpembed.add_field(name="Clear Messages", value="qt clear [amount to clear]", inline=True)
    helpembed.add_field(name="Unban", value="qt unban [user]", inline=True)
    helpembed.add_field(name="Server Info", value="qt server", inline=True)
    helpembed.add_field(name="Invite Link", value="qt invite", inline=True)
    helpembed.add_field(name="Dog Fact!", value="qt dog_fact", inline=True)
    helpembed.add_field(name="Cat Fact!", value="qt cat_fact", inline=True)
    helpembed.add_field(name="Hypixel Karma", value="qt karma <IGN>", inline=True)
    helpembed.add_field(name="Skywars Stats", value="qt swstats <IGN>", inline=True)
    helpembed.add_field(name="Bedwars Stats", value="qt bwstats <IGN>", inline=True)
    helpembed.set_footer(text='Message Olloz for more help!')

    await ctx.send(embed=helpembed)


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + ' Server Information',
        description=description,
        colour=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name='Owner', value=owner, inline=True)
    embed.add_field(name='Server ID', value=id, inline=True)
    embed.add_field(name='Region', value=region, inline=True)
    embed.add_field(name='Member Count', value=memberCount, inline=True)

    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    """Bot Invite"""
    await ctx.send("\U0001f44d")
    await ctx.send("Add me with this link {}".format(discord.utils.oauth_url(client.user.id)))


@client.command()
async def dog_fact(ctx):
    URL = 'https://some-random-api.ml/facts/dog'

    async with request('GET', URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data['fact'])


@client.command()
async def cat_fact(ctx):
    URL = 'https://some-random-api.ml/facts/cat'

    async with request('GET', URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data['fact'])


# HYPIXEL API#

@client.command()
async def karma(ctx, username):
    url = f'https://api.hypixel.net/player?key=631e3e7d-d02d-4e3e-94f0-be3a211beced&name={username}'

    async with aiohttp.request("GET", url) as response:
        if response.status == 200:
            data = await response.json()
            karma = data["player"]["karma"]
            await ctx.send(f'{karma:,}')


@client.command()
async def bwstats(ctx, username):
    url = f'https://api.hypixel.net/player?key=631e3e7d-d02d-4e3e-94f0-be3a211beced&name={username}'

    if True and len(username) >= 16:
        await ctx.send("Please enter a valid username.")
        return

    async with aiohttp.request("GET", url) as response:
        if response.status == 200:
            data = await response.json()
            star = data['player']['achievements']['bedwars_level']
            wins = data['player']['stats']['Bedwars']['wins_bedwars']
            losses = data['player']['stats']['Bedwars']['losses_bedwars']
            kills = data['player']['stats']['Bedwars']['kills_bedwars']
            deaths = data['player']['stats']['Bedwars']['deaths_bedwars']
            finals = data['player']['stats']['Bedwars']['final_kills_bedwars']

            bwembed = discord.Embed(title='Bedwars Stats', color=0x00fffb)
            bwembed.set_thumbnail(url="https://mineskin.de/armor/bust/" + username + "/100.png")
            bwembed.add_field(name=f'{username}\'s Bedwars Stats:',
                            value=(f'\n**Star**: {star}'
                                   f'\n**Wins**: {wins}'
                                   f'\n**Losses**: {losses}'
                                   f'\n**Kills**: {kills}'
                                   f'\n**Deaths**: {deaths}'
                                   f'\n**Final Kills**: {finals}'),
                              inline=False)

            await ctx.send(embed=bwembed)


@client.command()
async def swstats(ctx, username):
    url = f'https://api.hypixel.net/player?key=631e3e7d-d02d-4e3e-94f0-be3a211beced&name={username}'

    if True and len(username) >= 16:
        await ctx.send("Please enter a valid username.")
        return

    async with aiohttp.request("GET", url) as response:
        if response.status == 200:
            data = await response.json()
            swstar = data["player"]["achievements"]["skywars_you_re_a_star"]
            swwins = data['player']['stats']['SkyWars']['wins']
            swlosses = data['player']['stats']['SkyWars']['losses']
            swkills = data['player']['stats']['SkyWars']['kills']
            swdeaths = data['player']['stats']['SkyWars']['deaths']

            swembed = discord.Embed(title='Skywars Stats', color=0x00fffb)
            swembed.set_thumbnail(url="https://mineskin.de/armor/bust/" + username + "/100.png")
            swembed.add_field(name=f'{username}\'s Skywars Stats:',
                            value=(f'\n**Star**: {swstar}'
                                   f'\n**Wins**: {swwins}'
                                   f'\n**Losses**: {swlosses}'
                                   f'\n**Kills**: {swkills}'
                                   f'\n**Deaths**: {swdeaths}'),
                              inline=False)

            await ctx.send(embed=swembed)


@client.command()
async def stats(ctx, username):
    url = f'https://api.hypixel.net/player?key=API&name={username}'

    if True and len(username) >= 16:
        await ctx.send("Please enter a valid username.")
        return

    async with aiohttp.request("GET", url) as response:
        if response.status == 200:

            data = await response.json()
            exp = data["player"]["networkExp"]
            networklevel = (math.sqrt((2 * exp) + 30625) / 50) - 2.5
            networklevel = round(networklevel, 2)
            karma = data['player']['karma']

            totalquests = 0
            for lst in data["player"]["quests"]:
                for quest in data["player"]["quests"][lst]:
                    if quest == "completions":
                        for completion in data["player"]["quests"][lst]["completions"]:
                            totalquests += len(completion)

            uuid = data['player']['uuid']
            data2 = f'https://api.hypixel.net/friends?key=API&uuid={uuid}'
            totalFriends = 0
            async with aiohttp.request("GET", data2) as response2:
                if response2.status == 200:
                    friendsdata = await response2.json()
                    friends = friendsdata['records']
                    totalFriends = len(friends)

            sembed = discord.Embed(title='Hypixel Stats', color=0x00fffb)

            sembed.add_field(name=f'{username}\'s Stats:',
                            value=(f'\n**Level**: {networklevel}'
                                   f'\n**Karma**: {karma:,}'
                                   f'\n**Quests Completed**: {totalquests}'
                                   f'\n**Friends**: {totalFriends}')
                            .format(
                                str(networklevel),
                                str(totalquests),
                              inline=True))

            await ctx.send(embed=sembed)






client.run('CLIENTID')
