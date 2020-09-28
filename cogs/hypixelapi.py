import math
import json
import aiohttp
import discord
import discord.utils
from discord.utils import get
from discord.ext import commands

class hypixelapi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def karma(self, ctx, username):
        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:
                data = await response.json()
                karma = data["player"]["karma"]
                await ctx.send(f'{karma:,}')
                json_data.close()

    @commands.command()
    async def swstats(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

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
                swembed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                swembed.set_footer(text='Bot by: Olloz#0001')
                swembed.add_field(name=f'{username}\'s Skywars Stats:',
                                  value=(f'\n**Star**: {swstar:,}'
                                         f'\n**Wins**: {swwins:,}'
                                         f'\n**Losses**: {swlosses:,}'
                                         f'\n**Kills**: {swkills:,}'
                                         f'\n**Deaths**: {swdeaths:,}'),
                                  inline=False)

                await ctx.send(embed=swembed)
                json_data.close()

    @commands.command()
    async def bwstats(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

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
                bwembed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                bwembed.set_footer(text='Bot by: Olloz#0001')
                bwembed.add_field(name=f'{username}\'s Bedwars Stats:',
                                  value=(f'\n**Star**: {star:,}'
                                         f'\n**Wins**: {wins:,}'
                                         f'\n**Losses**: {losses:,}'
                                         f'\n**Kills**: {kills:,}'
                                         f'\n**Deaths**: {deaths:,}'
                                         f'\n**Final Kills**: {finals:,}'),
                                  inline=True)

                await ctx.send(embed=bwembed)
                json_data.close()

    @commands.command()
    async def stats(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

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
                if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
                    rank = data["player"]["rank"]
                elif "newPackageRank" in data["player"]:
                    rank = data["player"]["newPackageRank"]
                elif "packageRank" in data["player"]:
                    rank = data["player"]["packageRank"]
                else:
                    rank = "NON "
                if rank == "MVP_PLUS":
                    rank = "MVP+ "
                if rank == "VIP_PLUS":
                    rank = "VIP+ "

                uuid = data['player']['uuid']
                data2 = f'https://api.hypixel.net/friends?key={hypixeldata["hypixelKey"]}&uuid={uuid}'
                totalFriends = 0
                async with aiohttp.request("GET", data2) as response2:
                    if response2.status == 200:
                        friendsdata = await response2.json()
                        friends = friendsdata['records']
                        totalFriends = len(friends)

                sembed = discord.Embed(title='Hypixel Stats', color=0x00fffb)
                sembed.set_thumbnail(url="https://mineskin.de/armor/bust/" + username + "/100.png")
                sembed.set_image(url=f"https://gen.plancke.io/exp/" + username + ".png")
                sembed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                sembed.set_footer(text='Bot by: Olloz#0001')
                sembed.add_field(name=f'{rank}{username}\'s Stats:',
                                 value=(f'\n**Level**: {networklevel:,}'
                                        f'\n**Karma**: {karma:,}'
                                        f'\n**Quests Completed**: {totalquests:,}'
                                        f'\n**Friends**: {totalFriends:,}')
                                 .format(
                                     str(networklevel),
                                     str(totalquests),
                                     inline=True))

                await ctx.send(embed=sembed)
                json_data.close()

    @commands.command()
    async def skin(self, ctx, username):



        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        async with ctx.channel.typing():
            img = f"https://mineskin.de/armor/body/{username}/150.png"
            hypixelurl = f"https://api.hypixel.net/player?key={hypixeldata['hypixelKey']}&name={username}"

        async with aiohttp.request("GET", hypixelurl) as response:
            if response.status == 200:
                datas = await response.json()



                json_data = open('private.json')
                hypixeldata = json.load(json_data)

                displayname = datas["player"]["displayname"]
                skembed = discord.Embed(title='Skin', color=0x00fffb)
                skembed.set_footer(text="Bot by Olloz0001")
                skembed.set_author(name="Player Skin")
                skembed.set_image(url=img)
                skembed.add_field(name="\u200B",
                                value=f"**To dowload this skin click [__HERE__](https://mineskin.de/download/{username})**"
                                )

                await ctx.send(embed=skembed)
                json_data.close()
                return

    @commands.command()
    async def duelstats(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)
        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:

                data = await response.json()
                wins = data['player']['stats']['Duels']['wins']
                losses = data['player']['stats']['Duels']['losses']
                kills = data['player']['stats']['Duels']['kills']
                games = data['player']['stats']['Duels']['games_played_duels']
                duelsw_l = round(wins / losses, 2)
                duelsk_d = round(kills / losses, 2)

                dembed = discord.Embed(title=f'{username}\'s Duels Stats', color=0x00fffb)
                dembed.set_thumbnail(url="https://mineskin.de/armor/bust/" + username + "/100.png")
                dembed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                dembed.set_footer(text='Bot by: Olloz#0001')
                dembed.add_field(name=f'__Overall Stats__',
                                  value=(f'\n**Games Played**: {games:,}'
                                         f'\n**Total Wins**: {wins:,}'
                                         f'\n**Total Losses**: {losses:,}'                                   
                                         f'\n**Total Kills**: {kills:,}'
                                         f'\n**W/L**: {str (duelsw_l)}'
                                         f'\n**K/D**: {str (duelsk_d)}'))

                await ctx.send(embed=dembed)
                json_data.close()
                return

    @commands.command()
    async def bbstats(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:

                data = await response.json()
                wins = data['player']['stats']['BuildBattle']['wins']
                gamesplayed = data['player']['stats']['BuildBattle']['games_played']
                losses = (gamesplayed - wins)
                w_l = round(wins / losses, 2)
                prowins = data['player']['stats']['BuildBattle']['wins_solo_pro']

                bbembed = discord.Embed(title='Build Battle Stats', color=0x00fffb)
                bbembed.set_thumbnail(url="https://mineskin.de/armor/bust/" + username + "/100.png")
                bbembed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                bbembed.set_footer(text='Bot by: Olloz#0001')
                bbembed.add_field(name=f'{username}\'s Build Battle Stats',
                                 value=(f'\n**Wins**: {wins:,}'
                                        f'\n**Games Played**: {gamesplayed:,}'
                                        f'\n**Losses**: {losses:,}'
                                        f'\n**W/L**: {w_l:,}'
                                        f'\n**Pro Mode Wins**: {prowins:,}'))


                await ctx.send(embed=bbembed)
                json_data.close()
                return


    @commands.command()
    async def watchdog(self, ctx):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/watchdogstats?key={hypixeldata["hypixelKey"]}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:

                data = await response.json()
                wdtotal = data["watchdog_total"]
                stotal = data["staff_total"]
                total = (wdtotal + stotal)
                lastminute = data["watchdog_lastMinute"]

                embed = discord.Embed(title='Ban Stats', color=0x00fffb)
                embed.set_thumbnail(url="https://i.imgur.com/TLnWvw2.png")
                embed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                embed.set_footer(text='Bot by: Olloz#0001')
                embed.add_field(name='Hypixel Ban Stats',
                                value=(f'\n**Total Bans**: {total:,}'
                                       f'\n**Watchdog Bans**: {wdtotal:,}'
                                       f'\n**Staff Bans**: {stotal:,}'
                                       f'\n**Last Minute**: {lastminute:,}'))

                await ctx.send(embed=embed)
                json_data.close()
                return


    @commands.command()
    async def players(self, ctx):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)

        url = f'https://api.hypixel.net/gameCounts?key={hypixeldata["hypixelKey"]}'

        async with aiohttp.request("GET", url) as response:
            if response.status == 200:
                data = await response.json()
                total = data["playerCount"]
                mainlobby = data["games"]["MAIN_LOBBY"]["players"]
                skyblock = data["games"]["SKYBLOCK"]["players"]
                bw = data["games"]["BEDWARS"]["players"]
                sw = data["games"]["SKYWARS"]["players"]
                duels = data["games"]["DUELS"]["players"]
                arcade = data["games"]["ARCADE"]["players"]
                bb = data["games"]["BUILD_BATTLE"]["players"]
                pit = data["games"]["PIT"]["players"]
                housing = data["games"]["HOUSING"]["players"]
                limbo = data["games"]["LIMBO"]["players"]
                idle = data["games"]["IDLE"]["players"]

                embed = discord.Embed(title='Player Counts', color=0x00fffb)
                embed.set_thumbnail(url="https://i.imgur.com/TLnWvw2.png")
                embed.set_footer(icon_url='https://i.imgur.com/TLnWvw2.png')
                embed.set_footer(text='Bot by: Olloz#0001')
                embed.add_field(name='**Hypixel Live PLayer Counts**:',
                                value=(f'\n**Total Online**: {total:,}'
                                       f'\n**Main Lobby**: {mainlobby:,}'
                                       f'\n**Skyblock**: {skyblock:,}'
                                       f'\n**Bedwars**: {bw:,}'
                                       f'\n**Skywars**: {sw:,}'
                                       f'\n**Duels**: {duels:,}'
                                       f'\n**Arcade**: {arcade:,}'
                                       f'\n**Build Battle**: {bb:,}'
                                       f'\n**The Pit**: {pit:,}'
                                       f'\n**Housing**: {housing:,}'
                                       f'\n**Limbo**: {limbo:,}'
                                       f'\n**Idle**: {idle:,}'))

                await ctx.send(embed=embed)
                json_data.close()
                return

    @commands.command()
    async def verify(self, ctx, username):

        json_data = open('private.json')
        hypixeldata = json.load(json_data)
        url = f'https://api.hypixel.net/player?key={hypixeldata["hypixelKey"]}&name={username}'
        author = ctx.message.author
        async with aiohttp.request("GET", url) as response:
            if response.status == 200:
                data = await response.json()

                linked_discord = data["player"]["socialMedia"]["links"]["DISCORD"]

                if str(author) == linked_discord:
                    role = get(ctx.guild.roles, name="Verified")
                    await author.add_roles(role)

                    await ctx.send("Successfully Verified!")
                    print("Success")

                    print(author)
                    print(linked_discord)






def setup(bot):
    bot.add_cog(hypixelapi(bot))
