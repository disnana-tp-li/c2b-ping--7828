from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands


class Cat77C55458F8Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ping_thresholds = {}
        self.ping_log_channels = {}

    @app_commands.command(name="ping_alert_threshold", description="ping値が指定した閾値を超えた場合に警告を設定します。")
    async def ping_alert_threshold(self, interaction: discord.Interaction, value: str):
        try:
            threshold = int(value.replace("ms", ""))
            self.ping_thresholds[interaction.guild.id] = threshold
            await interaction.response.send_message(f"Ping alert threshold set to {threshold}ms for this server.")
        except ValueError:
            await interaction.response.send_message("Invalid threshold value. Please provide a number followed by 'ms', e.g., 200ms.")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")

    @app_commands.command(name="ping_log_channel", description="pingログを記録するチャンネルを設定します。")
    async def ping_log_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        self.ping_log_channels[interaction.guild.id] = channel.id
        await interaction.response.send_message(f"Ping logs will now be sent to {channel.mention}.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        try:
            if message.guild.id in self.ping_thresholds and message.guild.id in self.ping_log_channels:
                ping = round(self.bot.latency * 1000)
                threshold = self.ping_thresholds[message.guild.id]
                log_channel_id = self.ping_log_channels[message.guild.id]
                log_channel = self.bot.get_channel(log_channel_id)

                if ping > threshold:
                    embed = discord.Embed(title="Ping Alert!", color=discord.Color.red())
                    embed.add_field(name="Ping", value=f"{ping}ms", inline=False)
                    embed.add_field(name="Threshold", value=f"{threshold}ms", inline=False)
                    await log_channel.send(embed=embed)

        except Exception as e:
            print(f"Error in on_message: {e}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Cat77C55458F8Cog(bot))