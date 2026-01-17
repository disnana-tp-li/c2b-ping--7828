from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands
import random


class Cat0C9F6100EaCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.ping_data = []  # Store ping values (replace with database if needed)

    @app_commands.command(name="ping_stats", description="ping値の統計情報（平均、最大、最小）を表示します。")
    async def ping_stats(self, interaction: discord.Interaction):
        # Simulate ping data (replace with actual data source)
        self.ping_data = [random.randint(20, 150) for _ in range(10)]

        if not self.ping_data:
            await interaction.response.send_message("No ping data available.")
            return

        avg_ping = sum(self.ping_data) / len(self.ping_data)
        max_ping = max(self.ping_data)
        min_ping = min(self.ping_data)

        embed = discord.Embed(title="Ping Statistics", color=discord.Color.blue())
        embed.add_field(name="Average Ping", value=f"{avg_ping:.2f} ms", inline=False)
        embed.add_field(name="Maximum Ping", value=f"{max_ping} ms", inline=False)
        embed.add_field(name="Minimum Ping", value=f"{min_ping} ms", inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ping_outliers", description="異常なping値（外れ値）を検出します。")
    async def ping_outliers(self, interaction: discord.Interaction, period: str):
        # Simulate ping data for the specified period (replace with actual data source)
        if period == "1d":
            self.ping_data = [random.randint(20, 200) for _ in range(24)]  # Hourly data
        elif period == "7d":
            self.ping_data = [random.randint(20, 180) for _ in range(7)]  # Daily data
        elif period == "30d":
            self.ping_data = [random.randint(20, 160) for _ in range(30)]  # Daily data
        else:
            await interaction.response.send_message("Invalid period. Please use 1d, 7d, or 30d.")
            return

        if not self.ping_data:
            await interaction.response.send_message("No ping data available for this period.")
            return

        # Calculate mean and standard deviation
        mean_ping = sum(self.ping_data) / len(self.ping_data)
        std_dev = (sum([(x - mean_ping) ** 2 for x in self.ping_data]) / len(self.ping_data)) ** 0.5

        # Identify outliers (values outside 2 standard deviations)
        outliers = [x for x in self.ping_data if abs(x - mean_ping) > 2 * std_dev]

        if outliers:
            embed = discord.Embed(title="Ping Outliers", color=discord.Color.red())
            embed.add_field(name="Period", value=period, inline=False)
            embed.add_field(name="Outliers (ms)", value=", ".join(map(str, outliers)), inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("No ping outliers detected for this period.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Cat0C9F6100EaCog(bot))