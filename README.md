# Kimiko

Kimiko is a Discord bot developed with `discord.py` that offers various useful commands, user interaction, and dynamic status features.

## Features

> ⚠️ Remember to change your bot's prefix.

- **User Commands:**
  - `ping`: Returns the bot's latency.
  - `help`: Returns a help message.

## Technologies Used

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/en/stable/) for bot development
- [asyncio](https://docs.python.org/3/library/asyncio.html) for asynchronous execution
- [python-dotenv](https://pypi.org/project/python-dotenv/) for reading secrets
- [openai](https://developers.openai.com/api/docs) for AI responses

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/pedroosamp/Kimiko.git
   ```

2. Rename `.env.example` to `.env` and configure:
   ```env
   token=BOT_TOKEN
   prefix=.
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```

   Windows:
   ```bash
   ./venv/Scripts/Activate.ps1
   ```

   Linux:
   ```bash
   source ./venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the bot:
   ```bash
   python main.py
   ```
## License

Copyright (C) 2026 pedroosamp

Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).
See the [LICENSE](LICENSE) file for details.
