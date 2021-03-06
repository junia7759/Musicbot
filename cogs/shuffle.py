from discord.ext import commands

from utils import formatDuration

from . import check_voice_connection


class Shuffle(commands.Cog):
    def __init__(self, Bot) -> None:
        self.Bot = Bot

    @commands.command(name="shuffle")
    @commands.check(check_voice_connection)
    async def shuffle(self, ctx) -> None:
        VC = self.Bot.Audio.getVC(ctx.guild.id)
        Queue: dict = await VC.getQueue()

        if not Queue:
            return await ctx.send("> π΅  μνν  λΈλκ° λκΈ°μ΄μ μμ΄μ!")

        await VC.shuffle()

        return await ctx.send(f"> π΅  μ¬μλͺ©λ‘μ μλ λΈλ {len(Queue)} κ°λ₯Ό μννμ΄μ!")


def setup(Bot):
    Bot.add_cog(Shuffle(Bot))
