import logging
import os
import re
import traceback
from typing import Any

log = logging.getLogger("musicbot.cogs")

Directory = os.path.dirname(os.path.realpath(__file__))


def load(Bot):
    Failed = []

    for Extension in [
        "cogs." + re.sub(".py", "", File)
        for File in os.listdir(Directory)
        if not "__" in File
    ]:
        try:
            Bot.load_extension(Extension)
        except:
            log.error(f"while loading extension {Extension}, an error occured.")
            traceback.print_exc()
            Failed.append(Extension)

    return Failed


async def check_voice_connection(ctx) -> Any:
    if not ctx.bot.Audio.getVC(ctx.guild.id, safe=True):
        if not ctx.author.voice:
            await ctx.send("> π΅  λ¨Όμ  μμ± μ±λμ μ μν΄μ£ΌμΈμ!")
            return False

        message = await ctx.send(
            f"> π‘  μμ± μ±λ {ctx.author.voice.channel.mention} μ μ μ μ€..."
        )
        await ctx.bot.Audio.connect(ctx.author.voice.channel)
        await message.edit(
            content=f"> π΅  μ±κ³΅μ μΌλ‘ μμ± μ±λ {ctx.author.voice.channel.mention} μ μ μνμ΄μ!"
        )

    VC = ctx.bot.Audio.getVC(ctx.guild.id, safe=True)
    if VC and not hasattr(VC, "channel"):
        VC.channel = ctx.channel

    return True


async def only_in_voice(ctx) -> Any:
    if not ctx.bot.Audio.getVC(ctx.guild.id, safe=True):
        await ctx.send("> β  μ΄ λͺλ Ήμ΄λ λΈλ μ¬μ μ€μλ§ μ¬μ©μ΄ κ°λ₯ν λͺλ Ήμ΄μμ.")
        return False

    return True
