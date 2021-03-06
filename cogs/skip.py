from discord.ext import commands

from utils import formatDuration

from . import check_voice_connection


class Skip(commands.Cog):
    def __init__(self, Bot) -> None:
        self.Bot = Bot

    @commands.command(name="skip")
    @commands.check(check_voice_connection)
    async def skip(self, ctx) -> None:
        VC = self.Bot.Audio.getVC(ctx.guild.id)
        State: dict = await VC.getState()

        if not State.get("current"):
            return await ctx.send("> π΅  νμ¬ λΈλλ₯Ό μ¬μμ€μ΄μ§ μμμ!")

        await VC.skip()

        return await ctx.send(
            f'> π΅  **{State["current"]["title"]} [{formatDuration(State["duration"])}]** κ³‘μ΄ κ±΄λλ°μ΄μ‘μ΄μ!'
        )


def setup(Bot):
    Bot.add_cog(Skip(Bot))
