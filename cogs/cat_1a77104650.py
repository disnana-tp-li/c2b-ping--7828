from __future__ import annotations

import asyncio
import random

import discord
from discord import app_commands
from discord.ext import commands


class Cat1A77104650Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping_race", description="他のユーザーとping値を競います。")
    async def ping_race(self, interaction: discord.Interaction, users: str):
        user_list = users.split()
        ping_results = {}
        embed = discord.Embed(title="Ping Race Results", color=discord.Color.blue())

        for user_mention in user_list:
            try:
                user_id = int(user_mention[2:-1])  # Remove <@ and >
                user = await self.bot.fetch_user(user_id)
                ping = round(self.bot.latency * 1000)
                ping_results[user.name] = ping
            except Exception as e:
                embed.add_field(name=user_mention, value=f"Invalid user or unable to measure ping.", inline=False)
                print(f"Error processing user {user_mention}: {e}")
                continue

            embed.add_field(name=user.name, value=f"{ping}ms", inline=False)

        if ping_results:
            winner = min(ping_results, key=ping_results.get)
            winner_ping = ping_results[winner]
            embed.description = f"The winner is {winner} with a ping of {winner_ping}ms!"
        else:
            embed.description = "No valid users to determine a winner."

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ping_challenge", description="指定されたping値以内に収めるチャレンジを行います。")
    async def ping_challenge(self, interaction: discord.Interaction, target: int, time: int):
        embed = discord.Embed(title="Ping Challenge", color=discord.Color.green())
        embed.add_field(name="Target Ping", value=f"{target}ms", inline=False)
        embed.add_field(name="Time Limit", value=f"{time} seconds", inline=False)

        initial_ping = round(self.bot.latency * 1000)
        embed.add_field(name="Initial Ping", value=f"{initial_ping}ms", inline=False)

        success = True
        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < time:
            ping = round(self.bot.latency * 1000)
            if ping > target:
                success = False
                break
            await asyncio.sleep(0.5)

        final_ping = round(self.bot.latency * 1000)
        embed.add_field(name="Final Ping", value=f"{final_ping}ms", inline=False)

        if success:
            embed.description = f"Congratulations! You stayed within the target ping of {target}ms for {time} seconds."
        else:
            embed.description = f"Challenge failed. Your ping exceeded {target}ms during the challenge."

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Cat1A77104650Cog(bot))