import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!!", intents=intents)

CHANNEL_ID = 759506314371661864

@bot.event
async def on_ready():
    print(f"✅ Второй бот {bot.user} запущен!")
    asyncio.create_task(auto_join())

async def auto_join():
    while True:
        try:
            if not bot.voice_clients:
                channel = bot.get_channel(CHANNEL_ID)
                if channel:
                    # Простое подключение
                    await channel.connect(self_deaf=True, self_mute=True)
                    print(f"✅ Второй бот зашёл в {channel.name}")
        except Exception as e:
            print(f"Ошибка: {e}")
        await asyncio.sleep(20)

@bot.command()
async def join(ctx):
    await ctx.send("Попытка зайти...")
    if not ctx.author.voice:
        await ctx.send("❌ Ты не в войсе!")
        return
    try:
        await ctx.author.voice.channel.connect(self_deaf=True, self_mute=True)
        await ctx.send("✅ Зашёл!")
    except Exception as e:
        await ctx.send(f"Ошибка: {e}")

bot.run(os.getenv("TOKEN"))
