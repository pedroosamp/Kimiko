from utils.embed import create_embed
from config import PREFIX

async def command_not_found(ctx):
    return await create_embed(ctx=ctx,
        title="Command not found.",
        description=f"Send `{PREFIX}help` for more commands.")