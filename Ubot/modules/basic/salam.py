# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper.basic import edit_or_reply
from ubotlibs.ubot.helper.PyroHelpers import ReplyCheck


@Ubot("p", cmds)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Anak Anjing",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("pe", cmds)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("l", cmds)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Kaum Dajjal...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot("el", cmds)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )



@Ubot("as", cmds)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

add_command_help(
    "salam",
    [
        [f"p", "Assalamualaikum."],
        [f"pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        [f"l", "Wa'alaikumsalam."],
        [f"as", "Assalamualaikum Bahas arab."],
    ]
)
