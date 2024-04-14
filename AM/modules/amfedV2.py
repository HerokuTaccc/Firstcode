from AM import fban1 as ass
from pyrogram import Client, filters
from pyrogram.errors import ChatIdInvalid
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
import os
from pyrogram.enums import ParseMode
import json
from pyrogram.types import Message
from config import OWNER_ID, FBAN, UNFBAN, SUDO_USERS, APPEND, Doneapped
import asyncio
from pyrogram.types import Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import *
import logging
import os
import re
import random
from pyrogram.errors import (
    ChatAdminRequired
)
import random
import time
import requests
from pyrogram.enums import ChatAction, ParseMode

from datetime import datetime
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio
from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
import datetime
import asyncio

FBAN_LOGS = -1002143461069
AM = "6724520323"
F1 = "84388add-01c8-4bfa-bee0-3d0b9e42298f"
F2 = "c787613b-5e94-41b9-9d9b-1c7d383dd22d"
F3 = "16d688fb-553c-4e5e-91cf-166c67375d3c"
F4 = "1a84fef3-932a-434d-8b8e-32a3ecb0f974"

async def fban_user(client, message, user_id, reason):
    await client.send_message(FBAN_LOGS, f"/joinfed {F1}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F2}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F3}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F4}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)

async def unfban_user(client, message, user_id, reason):
    await client.send_message(FBAN_LOGS, f"/joinfed {F1}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F2}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F3}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F4}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)

@ass.on_message(filters.command(["superfban","massban","fban"], prefixes=["."]) & filters.user(SUDO_USERS))
async def fban_command(client, message):
    await message.delete() 
    try:
        user_id, reason = message.text.split(maxsplit=2)[1:]
        AMBOT = await message.reply(f"ɴᴇᴡ ꜱᴜᴘᴇʀʙᴀɴ ɪꜱ ɢᴏɪɴɢ...\nᴜꜱᴇʀ : `{user_id}`\nʙʏ : {message.from_user.mention}")
        await asyncio.sleep(2)
        await fban_user(client, message, user_id, reason)
        await AMBOT.edit(f"ꜱᴜᴘᴇʀʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ \nᴜꜱᴇʀ :{user_id}\nʀᴇᴀꜱᴏɴ : `{reason}`\n\n{FBAN}{message.from_user.mention}")
    except ValueError:
        await message.reply("Invalid format. Usev: `.superfban <user_id> <reason>`")


@ass.on_message(filters.command(["unfban","superunfban","massuban"], prefixes=["."]) & filters.user(SUDO_USERS))
async def unfban_command(client, message):
    await message.delete() 
    try:
        user_id, reason = message.text.split(maxsplit=2)[1:]
        UNFBANAMBOT = await message.reply(f"ɴᴇᴡ ꜱᴜᴘᴇʀᴜɴʙᴀɴ ɪꜱ ɢᴏɪɴɢ...\nᴜꜱᴇʀ : `{user_id}`\nʙʏ : {message.from_user.mention}")
        await asyncio.sleep(2)
        await unfban_user(client, message, user_id, reason)
        await UNFBANAMBOT.edit(f"ꜱᴜᴘᴇʀᴜɴʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ \nᴜꜱᴇʀ :{user_id}\nʀᴇᴀꜱᴏɴ : `{reason}`\n\n{UNFBAN}{message.from_user.mention}")
    except ValueError:
        await message.reply("Invalid format. Use: `.superunfban <user_id> <reason>`")
import psutil
import time
start_time = time.time()

def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp

@ass.on_message(filters.command(["ping","alive"], prefixes=["."]) & filters.user(OWNER_ID))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"ᴜᴘᴛɪᴍᴇ : {uptime} |ᴄᴘᴜ : {cpu}% "
    await message.reply(TEXT)
