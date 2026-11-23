import discord
from discord.ext import commands

from config import COMMANDS, PREFIX
from utils.embed import create_embed
from utils.helpers import remove_command_prefix
from utils.embed_messages import command_not_found

class Help(commands.Cog, description="Returns a help message."):
    name="Help"
    type="utils"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        arg = remove_command_prefix(ctx=ctx)
        if arg:
            command = await self.help_command(arg)
            if command:
                embed = await create_embed(ctx=ctx, title=arg.strip().capitalize(), description=command)
                return await ctx.reply(embed=embed)
            return await command_not_found(ctx)

        commands = await self.all_commands(ctx=ctx)
        await ctx.reply(commands)

    async def help_command(self, arg):
        return_command = ""
        for command in COMMANDS:
            if command["name"] == arg.strip().capitalize():
                return_command = (
                    f"**Usage:** `{PREFIX}{command["name"].lower()}`\n"
                    f"**Type:** {command["type"].capitalize()}\n"
                    f"**Description:** {command["description"]}"
                )
        return return_command

    async def all_commands(self, ctx):
        return_commands = ""
        types = []
        for command in COMMANDS:
            if command["type"] not in types:
                types.append(command["type"])
                return_commands += f"**{command["type"].capitalize()}**\n"
            return_commands += f"- {command["name"]}: {command["description"]}\n"
        return return_commands


async def setup(bot):
    await bot.add_cog(Help(bot))