import discord
from discord.ext import commands


class own(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.watching, name="qt help"))
        print('Bot is ready.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined! ')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left! ')


def setup(bot):
    bot.add_cog(own(bot))
