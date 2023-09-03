# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import time
import random
import speedtest
import asyncio
import re
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime
from . import *
from ubotlibs.ubot.helper.PyroHelpers import *
from Ubot import *
from Ubot.core.db import set_custom_var
from Ubot.core.cos_cmd import nay
from .systemstats import get_readable_time
from ubotlibs.ubot.utils.tools import get_arg


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply


class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"
    
kopi = [
    "**Hadir Sayang** 😍",
    "**Mmuaahh** 😘",
    "**Hadir** 🤗",
    "**Kenapa Sayangg?** 🥰",
    "**Iya Sayangg Kenapa?** 😘",
    "**Si paling absen ngentoddddd** 😒",
    "**Berisik lu kontollll 😏**",
]

roast = [
    "**DAR DER DOR, GC AMPAS KU GEDOR**",
    "**MEMBER SINI PADA KEBANYAKAN NGELEM**",
    "**BUBARIN AE GC AMPAS GINI MAH ANJING**",
    "**MANA NIH MEMBERNYA, GA ADA PERGERAKAN GINI**",
    "**LU TUH GA PANTES MAEN TELE SUMPAH, MENDING LU SEKOLAH YANG BENER**",
    "**SEKOLAH MASIH DI BIAYAIN PEMERINTAH AJA BELAGU LO KONTOL**",
    "**EALAH KACUNG TELE ANAKAN SINI YA**",
    "**BWAJINGAN**",
]
    
    
@Ubot(["speed"], cmds)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

@Client.on_message(
    filters.command(["absen"], "") & filters.user(DEVS) & ~filters.me
)
async def absen(client: Client, message: Message):
    await message.reply(random.choice(kopi))

@Client.on_message(
    filters.command(["aloo"], "") & filters.user(DEVS) & ~filters.me
)
async def roast(client: Client, message: Message):
    await message.reply("**Iyaa hlooo jugaa uputt gantengg 😍**")

@Client.on_message(
    filters.command(["Tod"], "") & filters.user(DEVS) & ~filters.me
)
async def tod(client, message):
    await message.reply("**Bacott luu ngentodddd!😏**")

@Client.on_message(
    filters.command(["uvuveveoasas"], "") & filters.user(DEVS) & ~filters.me
)
async def anara(client: Client, message: Message):
    await message.reply("**Punyaa Uputtt😘**")

@Client.on_message(filters.command("tes", [""]) & filters.user(DEVS))
async def tes(client, message: Message):
    await client.send_reaction(message.chat.id, message.id, "⚡")

@Client.on_message(
    filters.command("kping", [""]) & filters.user(DEVS) & ~filters.me
)
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    akhir = time.time()
    await message.reply_text(
      f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`"
      )
      
@Client.on_message(
    filters.command(["cping"], "") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], cmds) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply(f"❏ Pong!! <code>{duration}</code>\n╰ Active: <code>{uptime}</code>")

@nay(["hello"])
async def hello(client, message):
    await message.reply("hloo  sempak world")

@Client.on_message(
    filters.command("sv", ".") & filters.user(DEVS) & ~filters.me
)
async def setvar(client, message):
    user_id = client.me.id
    crot = await message.reply("`Processing...`")
    cok = get_arg(message)
    if not cok:
      return await crot.edit("`Give Variable and Value to set!`")
    else:
        biji = cok.split(" ", 1)
        await set_custom_var(user_id, var=biji[0], value=biji[1])
        await crot.edit(f"**Successfully Added Custom Var** \n\n**Var:** `{biji[0]}` \n**Val:** `{biji[1]}`")

"""
@nay(["pak"], CMD_HNDLR)
async def y(client, message):
    await message.reply("sesama gay itu monyet")


@Ubot("pek", "")
async def jing(client, message):
    ajg = await eor(message, "Modal copas Jing")
    await asyncio.sleep(2)
    await ajg.edit("Lah iya lu juga modal copas nyet")
    await asyncio.sleep(2)
    await ajg.edit("kok sok pro si bangsat")
    await asyncio.sleep(2)
    await ajg.edit("lah iya nyet sesama copas gausah hina bangsat")
    await asyncio.sleep(2)
    await ajg.edit("bahaha kok ngakak ajg")
    await asyncio.sleep(2)
    await ajg.edit("bangsat kok teriak bangsat")
    await asyncio.sleep(2)
    await ajg.edit("gay teriak gay **GOBLOK**")
"""
