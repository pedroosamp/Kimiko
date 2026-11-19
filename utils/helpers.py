

def remove_command_prefix(ctx):
    command = ctx.message.content.split()[0]
    return ctx.message.content.removeprefix(command).strip()