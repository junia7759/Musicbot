from discord.ext import commands

from . import check_voice_connection


class Volume(commands.Cog):
    def __init__(self, Bot) -> None:
        self.Bot = Bot

    @commands.command(name="volume", aliases=["vol"])
    @commands.check(check_voice_connection)
    async def volume(self, ctx, value: str = None) -> None:
        VC = self.Bot.Audio.getVC(ctx.guild.id)
        State: dict = await VC.getState()

        if value is None:
            return await ctx.send(
                f"> π  νμ¬ λ³Όλ₯¨ {round(State['options']['volume'] * 100)}%"
            )

        Operator: str = None
        if value.startswith(("+", "-")):
            Operator, volumeString = value[0], value[1:]
        else:
            volumeString = value

        if not volumeString.isdigit():
            return await ctx.send("β  λ³Όλ₯¨μ [+|-|μμ][λ³Όλ₯¨(μ μ)] μ νμλ§ μ¬μ© κ°λ₯ν΄μ!")

        Volume = State["options"]["volume"] * 100
        if Operator == "+":
            Volume += int(volumeString)
        elif Operator == "-":
            Volume -= int(volumeString)
        else:
            Volume = int(volumeString)

        if Volume > 200:
            return await ctx.send("β  λ³Όλ₯¨μ **200%** μ΄κ³ΌμΌμ μμ΄μ!")
        elif Volume <= 0:
            return await ctx.send("β  λ³Όλ₯¨μ μ΅μ **1%** μ¬μΌ ν΄μ!")

        await VC.setVolume(Volume / 100)

        return await ctx.send(f"> π  λ³Όλ₯¨μ΄ **{round(Volume)}%** λ‘ λ³κ²½λμμ΄μ!")


def setup(Bot):
    Bot.add_cog(Volume(Bot))
