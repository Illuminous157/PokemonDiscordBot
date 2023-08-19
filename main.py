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
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{args}")
            json = response.json()

            hp = json['stats'][0]['base_stat']
            attack = json['stats'][1]['base_stat']
            defense = json['stats'][2]['base_stat']
            special_attack = json['stats'][3]['base_stat']
            special_defense = json['stats'][4]['base_stat']
            speed = json['stats'][5]['base_stat']

            await ctx.send(f"Stats for {args}\n"
                           f"-------------------\n"
                           f"Attack: {attack}\n"
                           f"Defense: {defense}\n"
                           f"Special Attack: {special_attack}\n"
                           f"Special Defense: {special_defense}\n"
                           f"Speed: {speed}\n"
                           f"Hp: {hp}")
        except:
            await ctx.send(f"Unable to locate pokemon '{args}'.")

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()