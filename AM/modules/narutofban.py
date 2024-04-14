from AM import fban7  as ass
from pyrogram import Client, filters
from pyrogram.errors import ChatIdInvalid
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
import os
from pyrogram.enums import ParseMode
import json
from pyrogram.types import Message
from config import (
    OWNER_ID, 
    FBAN,
    UNFBAN,
    SUDO_USERS,
    APPEND,
    Doneapped,
)
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

FBAN_LOGS = -100199711166

F1 = "c6db37a3-f0e7-4962-ab55-e669c2366e31"
F2 = "bb629d37-6cde-4b4b-bba0-80419d06af41"
F3 = "d0b317e4-29fa-4874-937e-3b73caf53996"
F4 = "f297bd7a-dd4a-4eeb-99db-1ec20b25c4ae"
F5 = "8ad10b87-89d5-4054-a832-b4ce9a1d7314"
F6 = "c573a724-7264-4da4-8a2b-39bef95e2503"
F7 = "3a293f15-4185-41de-8924-77754ad7b7ec"
F8 = "2caaf1e7-210b-42b0-9e4e-ad44b5f28083"
F9 = "d0da563d-cdd6-40c5-8871-74d9a2d28685"
F10 = "d0da563d-cdd6-40c5-8871-74d9a2d28685"
F11 = "d0da563d-cdd6-40c5-8871-74d9a2d28685"
F12 = "8b0e14df-4679-4f50-88c5-e0cff6eb3aad"
F13 = "0a99fec4-6392-47f8-ad25-c05d2c0d69e9"
F14 = "1f86fc3a-62e4-439d-a3a1-a7e6a556821d"
F15 = "a5ed8f33-bc41-41e8-a3b6-1ed380617112"
F16 = "680371d7-acd6-4725-bb92-255635fb752b"
F17 = "e73935f8-d2ea-40db-ab15-10b9a58344c0"
F18 = "b4733f1b-8e8a-4a1c-8f94-4b9473feb0f0"
F19 = "ef055448-ab4a-42de-bed6-0bd60c1f497c"
F20 = "b21fae4e-cfcd-4630-997d-239e359a53ae"
F21 = "8bb70769-3e06-4fda-8059-c7b757376cfd"
F22 = "d1640fd7-2e6d-4d60-82a0-b4d82c786f25"


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
    await client.send_message(FBAN_LOGS, f"/joinfed {F5}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F6}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F7}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F8}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F9}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F10}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F11}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F12}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F13}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F14}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F15}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F16}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F17}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F18}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F19}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F20}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F21}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/fban {user_id} {reason}\n\n{FBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{APPEND}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F22}")
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
    await client.send_message(FBAN_LOGS, f"/joinfed {F5}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F6}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F7}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F8}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F9}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F10}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F11}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F12}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F13}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F14}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F15}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F16}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F17}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F18}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F19}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F20}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F21}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/unfban {user_id} {reason}\n\n{UNFBAN}<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n{Doneapped}")
    await asyncio.sleep(2)
    await client.send_message(FBAN_LOGS, f"/joinfed {F22}")
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
