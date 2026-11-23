import discord
from discord.ext import commands

import random

from utils.helpers import remove_command_prefix

class Roll(commands.Cog, description="Roll a dice"):
    name="Roll"
    type="fun"

    def __init__(self, bot):
        self.bot = bot

    def dice(self, sides: int = 6):
        if sides < 2:
            return (False, "You must roll at least 2 sides.")
        if sides > 100:
            return (False, "You can roll a maximum of 100 sides.")
        return random.randint(1, sides)

    @commands.command(name="roll")
    async def roll(self, ctx):
        arg = remove_command_prefix(ctx=ctx)
        result = 0

        try:
            if arg.isdigit():
                result = self.dice(sides=int(arg))
                if isinstance(result, tuple):
                    return await ctx.reply(result[1])
            elif "d" in arg:
                arg = arg.split("d")
                dices = int(arg[0]) if arg[0] else 1
                sides = int(arg[1]) if arg[1] else 6
                if dices > 100:
                    return await ctx.reply("You can roll a maximum of 100 dices at once.")
                if dices < 1:
                    return await ctx.reply("You must roll at least 1 dice.")
                
                results = [self.dice(sides=sides) for _ in range(dices)]
                error = next((r for r in results if isinstance(r, tuple)), None)
                if error:
                    return await ctx.reply(error[1])
                result = f"""{results} = {sum(results)}"""
            else:
                result = self.dice()
        except ValueError:
            return await ctx.reply("Invalid arguments. See how to use this command with `k!help roll`")
            
        return await ctx.reply(f"🎲 You rolled: **{result}**")

async def setup(bot):
    await bot.add_cog(Roll(bot))