import discord
from discord.ext import commands
from config import COMMANDS

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        util_commands = "\n".join(
            f"- {command.removeprefix("commands.utils.").capitalize()}: {description}"
            for command, description in COMMANDS.items()
            if "utils" in command
        )
        await ctx.reply(f"""
            # Commands
            ## Utils
            {util_commands}
        """)

async def setup(bot):
    await bot.add_cog(Help(bot))