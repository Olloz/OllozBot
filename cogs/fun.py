import random
from aiohttp import request
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f'Ping! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(pass_context=True)
    async def randomnumber(self, ctx):
        await ctx.send(random.randint(1, 101))

    @commands.command()
    async def panda(self, ctx):
        await ctx.send('**PANDA QT**')

    @commands.command()
    async def xynit(self, ctx):
        await ctx.send('**XYNIT**')

    @commands.command()
    async def gummy(self, ctx):
        await ctx.send('**GUMMY QT**')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

    @commands.command()
    async def dog_fact(self, ctx):
        URL = 'https://some-random-api.ml/facts/dog'

        async with request('GET', URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data['fact'])

    @commands.command()
    async def cat_fact(self, ctx):
        URL = 'https://some-random-api.ml/facts/cat'

        async with request('GET', URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data['fact'])

def setup(bot):
    bot.add_cog(fun(bot))