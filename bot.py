import discord
from discord.ext import commands
import asyncio
import random
from openai import OpenAI

# Configuration - Replace these with your own values
DISCORD_TOKEN = 'here'  # Your alt account's token
OPENAI_API_KEY = 'here'  # From OpenAI dashboard
TRIGGER_WORD = 'here'  # The word/phrase that triggers a response (e.g., your alt's username)
AI_MODEL = 'gpt-4o'  # GPT-4o model from OpenAI


openai_client = OpenAI(api_key=OPENAI_API_KEY)

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (Self-bot ready)')

@bot.event
async def on_message(message):
    
    if message.author.id == bot.user.id:
        return

    mentioned = bot.user.mentioned_in(message)
    replied = message.reference and message.reference.resolved and message.reference.resolved.author.id == bot.user.id
    triggered = TRIGGER_WORD.lower() in message.content.lower()
    is_dm = isinstance(message.channel, discord.DMChannel)

    if mentioned or replied or triggered or is_dm:
 
        async with message.channel.typing():
            await asyncio.sleep(random.randint(1, 5))


        chat_completion = openai_client.chat.completions.create(
            model=AI_MODEL,
            messages=[
                {"role": "system", "content": "Respond like a human in Discord. Keep it short no emoji. say something about the message the user sends or thoughts like what is on your mind, not conversational thoughts. don’t engage like a bot or anything just say something that matches to use as response. dont greet or say something conversational. respond always with a response based on the users response make sure its something about that response but in gen z style"},
                {"role": "user", "content": message.content}
            ]
        )
        ai_response = chat_completion.choices[0].message.content.strip()


        if is_dm or replied:
            await message.reply(ai_response, mention_author=False)
        else:
            await message.channel.send(ai_response)


bot.run(DISCORD_TOKEN)
# Note: Self-bots are against Discord's Terms of Service. Use at your own risk.
