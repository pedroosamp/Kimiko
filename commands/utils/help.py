import discord
from discord.ext import commands

from config import COMMANDS
from utils.embed import create_embed

class Help(commands.Cog, description="Returns a help message."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        util_commands = "\n".join(
            f"- {command.removeprefix("commands.utils.").capitalize()}: {description}"
            for command, description in COMMANDS.items()
            if "utils" in command
        )
    
        embed = await create_embed(
            ctx,
            "Commands",
            f"""
                **Utils**
                {util_commands}
            """
        )
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))