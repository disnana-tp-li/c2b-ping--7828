from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands
import matplotlib.pyplot as plt
import io
import random


class Cat7359432871Cog(commands.Cog, name="CreativeCog"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ping_data = {}

    def _get_ping_data(self, user_id: int) -> list[float]:
        return self.ping_data.get(user_id, [])

    def _add_ping(self, user_id: int, ping: float) -> None:
        if user_id not in self.ping_data:
            self.ping_data[user_id] = []
        self.ping_data[user_id].append(ping)

    @app_commands.command(name="ping_visualize", description="ping値の変動をグラフで視覚化します。")
    async def ping_visualize(self, interaction: discord.Interaction, period: str):
        await interaction.response.defer(thinking=True)
        user_id = interaction.user.id
        ping_values = self._get_ping_data(user_id)

        if not ping_values:
            await interaction.followup.send("No ping data available for visualization.")
            return

        # Basic error handling for period
        try:
            period_int = int(period[:-1])  # e.g., '1h' -> 1
            period_unit = period[-1]  # e.g., '1h' -> 'h'
        except ValueError:
            await interaction.followup.send("Invalid period format. Please use a format like '1h', '1d', or '1w'.")
            return

        if period_unit not in ['h', 'd', 'w']:
            await interaction.followup.send("Invalid period unit. Use 'h' for hours, 'd' for days, or 'w' for weeks.")
            return

        # Limit the data based on the period.  This is a simplification.
        if period_unit == 'h':
            max_points = period_int * 60  # Assuming one ping per minute
        elif period_unit == 'd':
            max_points = period_int * 1440  # Assuming one ping per minute
        else:
            max_points = period_int * 10080  # Assuming one ping per minute

        if len(ping_values) > max_points:
            ping_values = ping_values[-max_points:]

        plt.figure(figsize=(10, 5))
        plt.plot(ping_values)
        plt.xlabel("Time")
        plt.ylabel("Ping (ms)")
        plt.title(f"Ping Visualization ({period})")
        plt.grid(True)

        # Save the plot to a BytesIO object
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        plt.close()

        # Create a discord.File object from the buffer
        file = discord.File(img_buffer, filename="ping_graph.png")

        # Send the file as a response
        await interaction.followup.send(file=file)

    @app_commands.command(name="ping_history", description="過去のping値の履歴を表示します。")
    async def ping_history(self, interaction: discord.Interaction, count: int):
        user_id = interaction.user.id
        ping_values = self._get_ping_data(user_id)

        if not ping_values:
            await interaction.response.send_message("No ping history available.")
            return

        num_pings = min(count, len(ping_values))
        recent_pings = ping_values[-num_pings:]

        embed = discord.Embed(title="Ping History", color=discord.Color.blue())
        embed.add_field(name="Recent Pings", value="\n".join(f"{ping:.2f}ms" for ping in recent_pings), inline=False)
        embed.set_footer(text=f"Displaying last {num_pings} pings")

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Cat7359432871Cog(bot))