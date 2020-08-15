import discord
from discord.ext import commands
import random
import requests

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # get a random kaomoji bear
    # usage: >>bear
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bear(self, ctx):
        bears = ["ʕ •ᴥ•ʔ", "ᶘ ᵒᴥᵒᶅ", "ᶘ ⊙ᴥ⊙ᶅ", "ᶘ °㉨°ᶅ", "ᶘಠᴥಠᶅ", "ʕ •́؈•̀)", "ʕ´ڡ｀*ʔ", "ʕ – _ – ʔ", "ʕ – o – ʔ", "（´•(ｪ)•｀）", "ʕ≧(ｴ)≦ ʔ",
                "ʕ •㉨• ʔ", "ʕó㉨òʔﾉ♡", "ᶘ ᵒ㉨ᵒᶅ", "ʕ´•㉨•`ʔ", "ʕ≧㉨≦ʔ", "ʕ✪㉨✪ʔ", "ʕ ̿–㉨ ̿– ʔ", "ʕ/　·ᴥ·ʔ/", "ʕ； •`ᴥ•´ʔ", "ʕ ˵• ₒ •˵ ʔ",
                "ʕ •ᴥ•ʔゝ☆", "ᕕʕ •ₒ• ʔ୨", "ʕ　·ᴥʔ", "ʕ·ᴥ·　ʔ", "ʕᴥ·　ʔ", "ʕ •ᴥ•ʔ", "ʕง•ᴥ•ʔง"]
        await ctx.send(" " + random.choice(bears))

    # get a random cute picture of a cat
    # usage: >>cat
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(self, ctx):
        url = 'https://some-random-api.ml/img/cat'
        result_url = requests.get(url)
        resultjson=result_url.json()
        embed=discord.Embed(title="here is cat", description="cat",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text=f"a amazing good cat")
        await ctx.send(embed=embed)

    # get a random cute picture of a dog
    # usage: >>dog
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dog(self, ctx):
        url = 'https://some-random-api.ml/img/dog'
        result_url = requests.get(url)
        resultjson=result_url.json()
        embed=discord.Embed(title="here is dog", description="dog",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text=f"a amazing good dog")
        await ctx.send(embed=embed)

    # get a random picture of a meme
    # usage: >>meme
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def meme(self, ctx):
        url = 'https://some-random-api.ml/meme'
        result_url = requests.get(url)
        resultjson=result_url.json()
        embed=discord.Embed(title=resultjson['caption'], colour=discord.Colour.purple())
        embed.set_image(url=resultjson['image'])
        embed.set_footer(text=f"Category: {resultjson[ 'category']}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
