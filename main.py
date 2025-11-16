import os
from discord.ext import commands
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = commands.Bot(command_prefix="!", intents=commands.Intents.all())
client = Groq(api_key=GROQ_API_KEY)

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def ai(ctx, *, prompt):
    try:
        msg = await ctx.send("⏳ Sedang memikirkan jawaban...")

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )

        answer = response.choices[0].message["content"]
        await msg.edit(content=answer)

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

bot.run(DISCORD_TOKEN)
