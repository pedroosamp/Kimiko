import discord
import asyncio
from discord.ext import commands

from config import TOKEN, PREFIX, COMMANDS
import os


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix=PREFIX,
            intents=intents
        )

        self.remove_command("help")

    async def setup_hook(self):
        for root, dirs, files in os.walk("commands"):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    path = os.path.join(root, file)

                    extension = (
                        path.replace("./", "")
                        .replace("/", ".")
                        .replace("\\", ".")
                        .removesuffix(".py")
                    )
                    await self.load_extension(extension)
                    COMMANDS.update({extension: "No description"})

    async def on_ready(self):
        print(f"Logged as {self.user}")

        presences = [
            discord.Game(f"Send {PREFIX} help for more info!"),
            discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.guilds)} servers")
        ]
        count = 0
        while True:
            await self.change_presence(status=discord.Status.idle, activity=presences[count])
            await asyncio.sleep(4)
            count = (count + 1) % len(presences)
            

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == self.user.mention:
            await message.channel.send(
                f"Hi, send `{PREFIX}help` for commands."
            )

        await self.process_commands(message)

bot = Bot()
bot.run(TOKEN)