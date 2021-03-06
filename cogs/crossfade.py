from discord.ext import commands

from . import check_voice_connection


class Crossfade(commands.Cog):
    def __init__(self, Bot) -> None:
        self.Bot = Bot

    @commands.command(name="crossfade", aliases=["cf"])
    @commands.check(check_voice_connection)
    async def crossfade(self, ctx, value: str = None) -> None:
        VC = self.Bot.Audio.getVC(ctx.guild.id)
        State: dict = await VC.getState()

        if value is None:
            return await ctx.send(
                f"> π  νμ¬ ν¬λ‘μ€νμ΄λ {State['options']['crossfade']:.1f}μ΄"
            )

        Operator: str = None
        if value.startswith(("+", "-")):
            Operator, crossfadeString = value[0], value[1:]
        else:
            crossfadeString = value

        if not crossfadeString.isdigit():
            return await ctx.send("β  ν¬λ‘μ€νμ΄λλ [+|-|μμ][μ΄] μ νμλ§ μ¬μ© κ°λ₯ν΄μ!")

        Crossfade = State["options"]["crossfade"]
        if Operator == "+":
            Crossfade += float(crossfadeString)
        elif Operator == "-":
            Crossfade -= float(crossfadeString)
        else:
            Crossfade = float(crossfadeString)

        if Crossfade > 30:
            return await ctx.send("β  ν¬λ‘μ€νμ΄λλ **30μ΄** μ΄κ³ΌμΌμ μμ΄μ!")
        elif Crossfade < 0:
            return await ctx.send("β  ν¬λ‘μ€νμ΄λλ μ΅μ **0μ΄** μ¬μΌ ν΄μ!")

        await VC.setCrossfade(Crossfade)

        return await ctx.send(f"> π  ν¬λ‘μ€νμ΄λκ° **{Crossfade:.1f}** λ‘ λ³κ²½λμμ΄μ!")


def setup(Bot):
    Bot.add_cog(Crossfade(Bot))
