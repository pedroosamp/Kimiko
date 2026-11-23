import discord
from discord.ext import commands

from utils.embed import create_embed

class Avatar(commands.Cog, description="Returns an user's avatar picture."):
    name="Avatar"
    type="utils"
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, user: discord.User = None):
        if not user: user = ctx.author

        embed = await create_embed(ctx=ctx,
            title=user.display_name,
            image_url=user.display_avatar.url,
        )
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Avatar(bot))