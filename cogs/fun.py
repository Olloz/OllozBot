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
    async def banolloz(self, ctx):
        await ctx.send('**I have banned Olloz.**')

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
    async def ez(self, ctx):
        responses = ["Wait... This isn't what I typed!",
                     "Anyone else really like Rick Astley?",
                     "Hey helper, how play game?",
                     "Sometimes I sing soppy, love songs in the car.",
                     "I like long walks on the beach and playing Hypixel",
                     "Please go easy on me, this is my first game!",
                     "You're a great person! Do you want to play some Hypixel games with me?",
                     "In my free time I like to watch cat videos on Youtube",
                     "When I saw the witch with the potion, I knew there was trouble brewing.",
                     "If the Minecraft world is infinite, how is the sun spinning around it?",
                     "Hello everyone! I am an innocent player who loves everything Hypixel.",
                     "Plz give me doggo memes!",
                     "I heard you like Minecraft, so I built a computer in Minecraft in your Minecraft so you can Minecraft while you Minecraft",
                     "Why can't the Ender Dragon read a book? Because he always starts at the End.",
                     "Maybe we can have a rematch?",
                     "I sometimes try to say bad things then this happens :(",
                     "Behold, the great and powerful, my magnificent and almighty nemisis!",
                     "Doin a bamboozle fren.",
                     "Your clicks per second are godly. :eek:",
                     "What happens if I add chocolate milk to macaroni and cheese?",
                     "Can you paint with all the colors of the wind",
                     "Blue is greener than purple for sure",
                     "I had something to say, then I forgot it.",
                     "When nothing is right, go left.",
                     "I need help, teach me how to play!",
                     "Your personality shines brighter than the sun.",
                     "You are very good at the game friend.",
                     "I like pineapple on my pizza",
                     "I like pasta, do you prefer nachos?",
                     "I like Minecraft pvp but you are truly better than me!",
                     "I have really enjoyed playing with you! <3",
                     "ILY <3",
                     "Pineapple doesn't go on pizza!",
                     "Lets be friends instead of fighting okay?"]
        await ctx.send(f'{random.choice(responses)}')


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