import discord

async def create_embed(ctx, title=None, description=None, image_url=None, url=None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.yellow(),
        url=url
    )
    embed.set_image(url=image_url)

    if ctx.author.avatar:
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    else:
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.default_avatar.url)
    return embed