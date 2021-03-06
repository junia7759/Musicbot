from discord.ext import commands

from . import only_in_voice


class Stop(commands.Cog):
    def __init__(self, Bot) -> None:
        self.Bot = Bot

    @commands.command(name="stop")
    @commands.check(only_in_voice)
    async def stop(self, ctx) -> None:
        VC = self.Bot.Audio.getVC(ctx.guild.id)

        await VC.destroy()

        await ctx.send("> π΅  μ¬μμ€μΈ μμμ μ μ§νκ³  λκΈ°μ΄μ μ΄κΈ°ννμ΄μ!")


def setup(Bot):
    Bot.add_cog(Stop(Bot))
