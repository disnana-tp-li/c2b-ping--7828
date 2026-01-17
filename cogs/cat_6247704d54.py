from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands
import time


class Cat6247704D54Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping_check", description="サーバーとの接続速度を測定します。")
    async def ping_check(self, interaction: discord.Interaction):
        # Measure the bot's latency using discord.py's `latency` attribute.
        # Respond with an embed showing the latency in milliseconds.
        # Use a green color for the embed.
        # Include the user's avatar in the embed.
        start_time = time.time()
        await interaction.response.defer()
        end_time = time.time()
        latency_ms = round((end_time - start_time) * 1000)

        embed = discord.Embed(title="Ping Check", color=discord.Color.green())
        embed.add_field(name="Latency", value=f"{latency_ms}ms", inline=False)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="ping_average", description="一定期間の平均ping値を表示します。")
    async def ping_average(self, interaction: discord.Interaction, period: str):
        # Accept a 'period' argument (e.g., 10m, 1h, 1d) to specify the time range.
        # Retrieve historical ping data from a data store (e.g., a list or database).
        # Calculate the average ping value for the specified period.
        # Respond with an embed showing the average ping value and the period.
        # Use a blue color for the embed.
        # Handle cases where there is insufficient data for the specified period.
        # For simplicity, we'll use a hardcoded list of ping values and a simplified period interpretation.
        await interaction.response.defer()
        ping_data = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]  # Example ping data in ms
        
        # Simplified period interpretation (assuming 'all' means use all available data)
        if period.lower() == 'all':
            relevant_data = ping_data
        else:
            await interaction.followup.send("Invalid period. Please use 'all'.")
            return

        if not relevant_data:
            await interaction.followup.send("No ping data available for the specified period.")
            return

        average_ping = sum(relevant_data) / len(relevant_data)

        embed = discord.Embed(title="Ping Average", color=discord.Color.blue())
        embed.add_field(name="Period", value=period, inline=False)
        embed.add_field(name="Average Ping", value=f"{average_ping:.2f}ms", inline=False)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Cat6247704D54Cog(bot))