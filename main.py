import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!!", intents=intents)   # !! чтобы не конфликтовал с первым

CHANNEL_ID = 759506314371661864   # ←←← ИЗМЕНИ НА ID ТВОЕГО ГОЛОСОВОГО КАНАЛА

@bot.event
async def on_ready():
    print(f"✅ Второй бот {bot.user} запущен!")
    asyncio.create_task(auto_voice())

async def auto_voice():
    while True:
        try:
            if not bot.voice_clients:   # если ещё не в войсе
                channel = bot.get_channel(CHANNEL_ID)
                if channel:
                    vc = await channel.connect(self_deaf=True, self_mute=True)
                    print(f"✅ Второй бот зашёл в {channel.name}")
        except Exception as e:
            print(f"Ошибка: {e}")
        
        await asyncio.sleep(20)  # проверяет каждые 20 секунд

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Второй бот вышел")
    else:
        await ctx.send("Второй бот не в войсе")

bot.run(os.getenv("TOKEN"))
