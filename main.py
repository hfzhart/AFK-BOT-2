import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True   # Очень важно!
intents.voice_states = True

bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Второй бот {bot.user} онлайн!")

@bot.command()
async def join(ctx):
    await ctx.send("✅ Команда !!join работает! Бот видит сообщения.")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Понг! Задержка: {round(bot.latency * 1000)}ms")

bot.run(os.getenv("TOKEN"))
