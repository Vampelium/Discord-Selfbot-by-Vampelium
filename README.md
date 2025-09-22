# Discord Selfbot Bot

Lightweight Discord self-bot that uses OpenAI's GPT-4o model to generate short, human-like responses when you get pinged, replied to, DM'd, or when a trigger phrase appears.

## Important Disclaimer
Running a self-bot is against Discord's Terms of Service and can lead to account termination. Proceed only if you understand and accept that risk. Use an alternate account and never expose your main account credentials.

## Prerequisites
- Python 3.10 or newer
- pip (comes with Python installs)
- OpenAI API key with access to the gpt-4o model
- Discord account token (preferably an alternate account)

## Setup
1. Clone or download this repository.
2. (Recommended) Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install discord.py openai python-dotenv
   ```
4. Configure secrets:
   - Open `bot.py` and replace the placeholder values for `DISCORD_TOKEN`, `OPENAI_API_KEY`, `TRIGGER_WORD`, and `AI_MODEL`.
   - Keep these secrets out of commits. If you prefer using environment variables, create a `.env` file (see below) and update the script to load from it before storing real keys.

### Optional `.env` template
```env
DISCORD_TOKEN=your-discord-token
OPENAI_API_KEY=sk-your-openai-key
TRIGGER_WORD=your-trigger
AI_MODEL=gpt-4o
```

## Running the bot
```powershell
python bot.py
```
Once logged in, the console prints the account name. The bot watches for mentions, replies, DMs, and the configured trigger word, then replies with an OpenAI-generated message after a short typing delay.

## Tips
- Adjust the system prompt inside `bot.py` to fine-tune the voice and behaviour.
- Rate limits apply on both Discord and OpenAI. Monitor usage and back off if you see errors.
- Never share tokens or API keys. Rotate keys immediately if they leak.
