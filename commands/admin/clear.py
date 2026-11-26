import discord
from discord.ext import commands

from utils.helpers import remove_command_prefix
from utils.embed import create_embed

class Clear(commands.Cog, description="Clear a specified number of messages from a channel."):
    name="Clear"
    type="admin"
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx):
        amount = remove_command_prefix(ctx=ctx)
        if amount.isdigit():
            amount = int(amount)
            if amount < 1:
                return await ctx.reply("The minimum number of messages to clear is 1.")
            if amount > 100:
                return await ctx.reply("The maximum number of messages to clear is 100.")

            deleted = await ctx.channel.purge(limit=amount)
            embed = await create_embed(ctx=ctx, description=f"**{len(deleted)} messages cleared.**")
            await ctx.send(embed=embed)
        else:
            await ctx.reply("You must specify a valid number of messages to clear.")

async def setup(bot):
    await bot.add_cog(Clear(bot))