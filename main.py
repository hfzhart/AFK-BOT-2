import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!!", intents=intents)

CHANNEL_ID = 759506314371661864   # Твой канал

@bot.event
async def on_ready():
    print(f"✅ Второй бот {bot.user} запущен!")
    asyncio.create_task(auto_join())

async def auto_join():
    """Автоматически заходит в канал"""
    while True:
        try:
            if not bot.voice_clients:
                channel = bot.get_channel(CHANNEL_ID)
                if channel:
                    await channel.connect(self_deaf=True, self_mute=True)
                    print(f"✅ Авто-заход в канал: {channel.name}")
        except Exception as e:
            print(f"Ошибка авто-захода: {e}")
        await asyncio.sleep(20)

@bot.command()
async def join(ctx):
    """Ручной заход"""
    if ctx.voice_client:
        await ctx.send("✅ Я уже в войсе")
        return
    
    if not ctx.author.voice:
        await ctx.send("❌ Ты должен находиться в голосовом канале!")
        return

    channel = ctx.author.voice.channel
    try:
        await channel.connect(self_deaf=True, self_mute=True)
        await ctx.send(f"✅ Зашёл в **{channel.name}**")
    except Exception as e:
        await ctx.send(f"❌ Ошибка: {e}")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Вышел из войса")
    else:
        await ctx.send("Я не в войсе")

bot.run(os.getenv("TOKEN"))
