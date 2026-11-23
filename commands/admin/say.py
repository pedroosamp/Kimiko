import discord
from discord.ext import commands

from utils.helpers import remove_command_prefix

class Say(commands.Cog, description="Repeats the users text"):
    name="Say"
    type="admin"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="say")
    async def say(self, ctx):
        if not ctx.author.guild_permissions.manage_messages:
            return await ctx.channel.send(f"{ctx.author.mention} You must have the `Manage Messages` permission to run this command.")
        await ctx.send(remove_command_prefix(ctx=ctx))
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(Say(bot))