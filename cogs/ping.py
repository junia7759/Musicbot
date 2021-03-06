from datetime import datetime

import discord
from discord.ext.commands import Cog, command
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.message import Message


class Ping(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @command(name="ν")
    async def _ping(self, ctx: Context):
        msg: Message = await ctx.send(
            embed=discord.Embed(title="πν", description="μΈ‘μ μ€", colour=0x7289DA)
        )
        await msg.edit(
            embed=discord.Embed(
                title="πν!",
                description=f"μΉμμΌ ν: {round(self.bot.latency * 1000)}ms\nλ©μΈμ§ λ°μ ν: {round(msg.created_at - ctx.message.created_at).total_seconds()}ms",
                timestamp=datetime.utcnow(),
                colour=0x7289DA,
            )
        )


def setup(bot: Bot):
    bot.add_cog(Ping(bot))
