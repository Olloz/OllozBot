import discord
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
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

    @commands.command(pass_context=True)
    async def info(self, ctx):
        embed = discord.Embed(title="Olloz's Bot Info",
                              description="Olloz's Bot is a small bot made by Olloz!", color=0x00fffb)
        embed.add_field(name="Bot usage:", value="qt [command]", inline=False)
        embed.set_footer(text=":)")
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        helpembed = discord.Embed(title="Help Menu", description="**Prefix: 'qt'**", color=0x00fffb)
        helpembed.add_field(name="Help", value="qt help", inline=True)
        helpembed.add_field(name="Bot's Ping", value="qt ping / qt pong", inline=True)
        helpembed.add_field(name="User Info", value="qt whois [user]", inline=True)
        helpembed.add_field(name="Am I qt?", value="*Being Developed*", inline=True)
        helpembed.add_field(name="8 Ball", value="qt 8ball [question]", inline=True)
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
        helpembed.add_field(name="Hypixel Stats", value="qt stats <IGN>", inline=True)
        helpembed.add_field(name="Skin", value="qt skin <IGN>", inline=True)
        helpembed.set_footer(text='Message Olloz for more help!')

        await ctx.send(embed=helpembed)

    @commands.command()
    async def server(self, ctx):
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

    @commands.command()
    async def invite(self, ctx):
        """Bot Invite"""
        await ctx.send("Add me with this link {}".format(discord.utils.oauth_url(self.bot.user.id)))

def setup(bot):
    bot.add_cog(misc(bot))
