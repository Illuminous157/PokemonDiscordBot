import settings
import discord
import requests
import json
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def love(ctx):
        await ctx.send("Emily Barton! <3")

    @bot.command()
    async def favorite(ctx):
        await ctx.send("Garchomp!")

    @bot.command()
    async def stats(ctx, args):
        message = ""
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args}")
            json = response.json()
            for stat in json['stats']:
                message += f"{stat['stat']['name']}: {stat['base_stat']}\n"
            await ctx.send(message)
        except:
            await ctx.send(f"Unable to locate pokemon '{args}'.")

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()