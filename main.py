import discord
from discord.ext import commands
from dotenv import load_dotenv

import os

from config import COMMANDS

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix=os.getenv("prefix"),
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
        print(f"Conectado como {self.user}")


bot = Bot()
bot.run(os.getenv("token"))