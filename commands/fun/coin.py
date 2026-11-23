import discord
from discord.ext import commands

import random
import asyncio

from utils.embed import create_embed

class Coin(commands.Cog, description="Toss a coin."):
    name="Coin"
    type="fun"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="coin")
    async def coin(self, ctx):
        result = random.randint(0, 1)

        if result == 1: result = "Heads 🪙!"
        else: result = "Tails 👑!"
        embed = await create_embed(ctx=ctx,
            description=f"🪙 <@{ctx.author.id}> **flipped a coin and got {result}**",
            image_url="https://c.tenor.com/f_tBstiZzBQAAAAd/tenor.gif"
        )
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Coin(bot))