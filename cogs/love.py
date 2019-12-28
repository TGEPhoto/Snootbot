import discord
from discord.ext import commands
import random

class Love(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def love(self, ctx):
        """
        Sends random love message
        """
        love = ['You are beautiful!',
                'You are epic',
                'I love you uwu',
                'You are wonderful',
                'I love you cutie',
                'You are cute',
                'ily comrade',
                'Message my creator to add more love!',
                'You’re more helpful than you realize.',
                'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.',
                'You are making a good difference in the world just by existing.',
                'Your existence alone makes peoples days better',
                'You bring out the best in other people',
                'When you are not afraid to be yourself is when you are most incredible',
                'I wish you realized how beautiful you are inside and out',
                'You are more fun than a ball pit filled with candy. And seriously, what could be more fun than that?',
                'You are better than a triple-scoop ice cream cone. Even with rainbow sprinkles',
                'This server is better because you’re in it',
                'You are more fun than bubble wrap',
                'You should be thanked more often. Thank you!']
        await ctx.send(random.choice(love))

    @commands.command()
    async def positivity(self, ctx):
        """
        Sends a random positive message
        """
        positive = ['Learn to light a candle in the darkest moments of someone’s life. Be the light that helps others see; it is what gives life its deepest significance.',
                    'Life is about accepting the challenges along the way, choosing to keep moving forward, and savoring the journey.',
                    'A random act of kindness, no matter how small, can make a tremendous impact on someone elses life.',
                    'Life becomes easier and more beautiful when we can see the good in other people.',
                    'Everyone is deserving of kindness. That includes you!',
                    'Follow your heart, listen to your inner voice, stop caring about what others think. You are you, if people cannot accept that they are not worth your time.',
                    'You have significance on this earth. Keep doing what you love and what you are passionate about, the world needs it.',
                    'Do what is right, not what is easy nor what',
                    'Accept yourself, love yourself, and keep moving forward. If you want to fly, you have to give up what weighs you down.',
                    'Everyone has flaws and imperfections. Thats what makes the world so different and beautiful.',
                    'Be the reason someone smiles. Be the reason someone feels loved and believes in the goodness in people.',
                    'You have survived 100% of your bad days. You can survive this one too. You are a lot stronger than you think you are.',
                    'More smiling, less worrying. More compassion, less judgment. More blessed, less stressed. More love, less hate.',
                    'Instead of worrying about what you cannot control, shift your energy to what you can create.',
                    'Dont be pushed around by the fears in your mind. Be led by the dreams in your heart.']
        await ctx.send(random.choice(positive))

def setup(client):
    client.add_cog(Love(client))