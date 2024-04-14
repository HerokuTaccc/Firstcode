from AM import fban6  as ass
from pyrogram import Client, filters
from pyrogram.errors import ChatIdInvalid
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
import os
from pyrogram.enums import ParseMode
import json
from pyrogram.types import Message
from config import (
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
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatIdInvalid
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
import os
from pyrogram.enums import ParseMode
import json
from pyrogram.types import Message
from config import ( 
    FBAN_LOGS,
    SUDO_USERS,
    Doneapped,
)
from typing import Union, Optional
import asyncio
from pyrogram.types import Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from gpytranslate import Translator
from telegraph import upload_file
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from PIL import Image, ImageEnhance
from pyrogram.types import *
import logging
import base64
import httpx
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
from platform import python_version as pyver
from pyrogram import __version__ as pver
from pyrogram.types import InputMediaPhoto
from AM.Helper.db.chatsdb import add_afk, is_afk, remove_afk
from AM import fban6  as rais

FBAN_LOGS = -1002137723828
RAI = 6297223639
F1 = "7658f47c-b045-4a63-bdd1-1f3ad57d29e5"
F2 = "e73935f8-d2ea-40db-ab15-10b9a58344c0"
F3 = "5ea230d9-ebbc-4397-8fa5-af8a80f94300"
F4 = "61c56607-ea7d-4893-9d4f-770cd63d7626"
F5 = "4e74f40a-9a06-4b1d-8c99-d6fa07407125"
F6 = "3d14f541-de49-4f6a-aea6-b8bd189ef9cf"
F7 = "99e59084-4bfa-4f2e-a1e3-29feb629906f"
F8 = "54865e26-78de-45d6-953f-6ea15ddef1c4"
F9 = "28eab8ee-5892-420d-8d38-b7af081e1ec1"
F10 = "e2a195be-074f-476c-bb0d-21238bd3d2aa"
F11 = "e25593f1-2438-42da-a778-1d25e7313c0c"
F12 = "f4ab1eca-e77c-47eb-b89b-5535c5dbe74f"
F13 = "f4b119b4-0e89-4668-8323-c50cb63c23fa"
F14 = "10b20a32-a414-41d2-bc98-6c80bb406397"
F15 = "c573a724-7264-4da4-8a2b-39bef95e2503"
F16 = "74680425-49af-4da0-8273-599a11d09552"
F17 = "43366854-49b9-4815-acf4-cc1b19a8efd9"
F18 = "8466d7f3-d8ec-4c89-bded-9007fb3f98a2"
F19 = "7a8ea916-1a31-4acb-a0f6-25b9ebeef7f7"
F20 = "03cb7fc3-8d6b-4f39-9dec-c9a470a54f88"



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



#OTHER MODUALS

@ass.on_message(filters.command(["write", "pen"], prefixes=["."]) & filters.user(RAI))
async def activevc(_, message: Message):
        await message.delete() 
        if message.reply_to_message:
            text = message.reply_to_message.text
        else:
            try:
                _, text = message.text.split(maxsplit=1)
            except ValueError:
                return await message.reply("Please provide some text to write.")

        m = await message.reply_text("`Please wait...,\n\nWriting your text...`")

        write = requests.get(f"https://apis.xditya.me/write?text={text}").url

        caption = f"""
        💌 ᴡʀɪᴛᴛᴇɴ ʙʏ : {message.from_user.mention}
        """

        await m.delete()
        await message.reply_photo(photo=write, caption=caption)


@ass.on_message(filters.command(["fstat"], prefixes=["."]) & filters.user(RAI))
async def sg(client: Client, message: Message):
    await message.delete() 
    if len(message.text.split()) < 1 and not message.reply_to_message:
        return await message.reply("fstat username/id/reply")
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]
    lol = await message.reply("<code>Checking Fstats...</code>")
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>Please specify a valid user!</code>")
    bo = ["MissRose_bot", "MissRose_bot"]
    sg = random.choice(bo)
    
    try:
        a = await client.send_message(sg, f"/fstat {user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(e)
    await asyncio.sleep(1)
    
    async for stalk in client.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await message.reply("Error ReTry..")
        elif stalk:
            await message.reply(f"{stalk.text}")
            break  # Exit the loop after displaying one message
    
    try:
        user_info = await client.resolve_peer(sg)
        await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass
    
    await lol.delete()


@ass.on_message(filters.command(["fedinfo"], prefixes=["."]) & filters.user(RAI))
async def sg(client: Client, message: Message):
    await message.delete()
    lol = await message.reply("<code>Checking FedInfo...</code>")
    bo = ["MissRose_bot", "MissRose_bot"]
    sg = random.choice(bo)
    try:
        text = message.text.split(' ', 1)[1]
        a = await client.send_message(sg, f"/fedInfo {text}")
        await a.delete()
    except IndexError:
        return await lol.edit("<code>Please specify a valid fedId!.</code>")
    except Exception as e:
        return await lol.edit(str(e))
    
    await asyncio.sleep(1)
    
    async for stalk in client.search_messages(a.chat.id):
        if stalk.text is None:
            continue
        if stalk:
            await message.reply(f"{stalk.text}")
            break  
    
    try:
        user_info = await client.resolve_peer(sg)
        await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass
    
    await lol.delete()


@ass.on_message(filters.command(["myfeds"], prefixes=["."]) & filters.user(RAI))
async def sg(client: Client, message: Message):
    await message.delete() 
    lol = await message.reply("<code>Checking FAdmins...</code>")
    bo = ["MissRose_bot", "MissRose_bot"]
    sg = random.choice(bo)
    
    try:
        a = await client.send_message(sg, f"/myfeds")
        await a.delete()
    except Exception as e:
        return await lol.edit(e)
    await asyncio.sleep(1)
    
    async for stalk in client.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await message.reply("Error ReTry..")
        elif stalk:
            await message.reply(f"{stalk.text}")
            break  # Exit the loop after displaying one message
    
    try:
        user_info = await client.resolve_peer(sg)
        await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass
    
    await lol.delete()



@ass.on_message(filters.command(["ask","chatgpt"], prefixes=["."]) & filters.user(RAI))
async def chat_gpt(bot, message):
    await message.delete()
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n.ask Where is TajMahal?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f" {x} \n\nᴀɴsᴡᴇʀɪɴɢ ʙʏ ➛ @New_AMBOT",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"Help AMBOT Bro: {e} ")

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

@ass.on_message(filters.command(["ping","alive"], prefixes=["."]) & filters.user(RAI))
async def activevc(_, message: Message):
    await message.delete()
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"ᴜᴘᴛɪᴍᴇ : {uptime} |ᴄᴘᴜ : {cpu}% "
    await message.reply(TEXT)


@ass.on_message(filters.command(["id"], prefixes=["."]) & filters.user(RAI))
async def getid(client, message):
    await message.delete()
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"[ᴍᴇssᴀɢᴇ ɪᴅ :]({message.link}) `{message_id}`\n"
    text += f"[ʏᴏᴜʀ ɪᴅ :](tg://user?id={your_id}) `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username}) `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link}) `{reply.id}`\n"
        text += f"[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id}) `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )

@ass.on_message(filters.command(["rulse","admin"], prefixes=["."]) & filters.user(RAI))
async def activevc(_, message: Message):
    await message.delete()
    TEXT = f""" 
ʜᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ ?
ᴀɴʏᴏɴᴇ ᴄᴀɴ ᴊᴏɪɴ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ʀᴇQᴜɪʀᴇᴍᴇɴᴛꜱ.

ᴡʜᴀᴛ ɪꜱ ʀᴇQᴜɪʀᴇᴍᴇɴᴛꜱ ꜰᴏʀ ᴊᴏɪɴɪɴɢ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ !!
1) 2 ꜰᴇᴅ ꜱᴜʙ ɪꜰ ᴜ ʜᴀᴠᴇ ꜰᴇᴅ ᴇʟɪꜰ ᴊᴏɪɴꜰᴇᴅ 3 
ꜰᴇᴅ ɪᴅ 1 : `/subfed 6c869a9b-5277-4da4-ad14-4fdbde69f517`
ꜰᴇᴅ ɪᴅ 2 : `/subfed 1a84fef3-932a-434d-8b8e-32a3ecb0f974`
ꜱᴜʙ ᴛʜɪꜱ 2 ꜰᴇᴅꜱ
2) ᴜ ʜᴀᴠᴇ ɴᴇᴇᴅ 15+ ꜰᴇᴅ ɪɴ ᴀᴅᴍɪɴꜱ 
3) ᴜꜱᴇ ʙᴀɴ ᴄᴏᴅᴇ ᴏᴜᴇ ꜱᴇ
VALID BAN CODE SHOULD BE USED 
PROOF SHOULD MATCH WITH BAN CODE
PROOF SHOULD BE VALID
WITHOUT BAN CODE AND PROOF SHOULD BE REMOVED IMMEDIATELY


 ʙᴇɴᴇꜰɪᴛꜱ
1. ɪꜰ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴀɴʏ ꜰᴇᴅ ᴏʀ ɪꜰ ᴛʜᴏꜱᴇ ꜰᴇᴅꜱ ᴀʀᴇ ɪɴ ᴏᴜʀ ᴛᴇᴀᴍ ᴛʜᴇɴ ʏᴏᴜʀ ʙᴀɴɴᴇᴅ ᴍᴇᴍʙᴇʀ ᴡɪʟʟ ᴀʟꜱᴏ ʙᴇ ʙᴀɴɴᴇᴅ.

2. ᴀꜱ ᴍᴀɴʏ ꜰᴇᴅꜱ ᴀꜱ ʏᴏᴜ ɢɪᴠᴇ ᴛᴏ ᴏᴜʀ ᴛᴇᴀᴍ ᴡɪᴛʜ ᴏɴᴇ ᴄᴏᴍᴍᴀɴᴅ, ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴅᴇꜰᴇᴀᴛᴇᴅ ʙʏ ᴀʟʟ ᴏꜰ ᴜꜱ.

{Doneapped }
    """
    await message.reply(TEXT)


@ass.on_message(filters.command(["tgm","telegraph"], prefixes=["."]) & filters.user(RAI))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("`Processing...`")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')


trans = Translator()

@ass.on_message(filters.command(["tr","trt"], prefixes=["."]) & filters.user(RAI))
async def translate(_, message) -> None:
    await message.delete()
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ !")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} to {dest}:\n"
        f"{translation.text}"
    )
    await message.reply_text(reply)

async def get_user_profile_photo(RAI):
    try:
        user_info = await ass.get_chat(RAI)
        user = await ass.get_users(RAI)
        if user.photo:
            # Download the user's profile photo
            profile_photo = await ass.download_media(user.photo.big_file_id)
            return profile_photo
        else:
            return None
    except Exception as e:
        print(f"Error occurred while getting profile photo: {e}")
        return None

@ass.on_message(filters.command(["help","cmds","cmd"], prefixes=["."]) & filters.user(RAI))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴛᴇᴀᴍ")
    await asyncio.sleep(1)
    await accha.edit("ꜱᴜᴘᴇʀʙᴀɴ")
    await asyncio.sleep(1)
    await accha.edit("ᴛᴇᴀᴍ ꨄ︎ ꜱᴜᴘᴇʀʙᴀɴ")
    await accha.delete()
    await asyncio.sleep(0.3)
    bot_info = await client.get_me()
    bot_username = bot_info.username
    profile_photo = await get_user_profile_photo(RAI)
    if profile_photo:
        umm = await m.reply_photo(
            photo=profile_photo,
            caption=f"""ʜᴇʏ, ɪ ᴀᴍ 『[{bot_info.first_name}](https://t.me/{bot_username})』
   ━━━━━━━━━━━━━━━━━━━
ʜᴇʀᴇ ɪꜱ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ  ᴍᴇɴᴜ :
»`.superfban` ᴜꜱᴇʀɪᴅ / ᴜꜱᴇɴᴀᴍᴇ ʀᴇᴀꜱᴏɴ : ꜰᴏʀ ꜱᴜᴘᴇʀʙᴀɴ
»`.superunfban` ᴜꜱᴇʀɪᴅ / ᴜꜱᴇɴᴀᴍᴇ ʀᴇᴀꜱᴏɴ : ꜰᴏʀ ꜱᴜᴘᴇʀᴜɴʙᴀɴ  
»`.pen` : ᴡʀɪᴛᴇ ꜱᴏᴍᴇᴛɪɴɢ..
»`.fstat` : ɢɪᴠᴇꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ'ꜱ ʙᴀɴ ɪɴ ᴀ ꜰᴇᴅᴇʀᴀᴛɪᴏɴ.
»`.fedinfo` : ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ꜰᴇᴅᴇʀᴀᴛɪᴏɴ.
»`.myfeds` : ʟɪꜱᴛ ᴀʟʟ ꜰᴇᴅꜱ ʏᴏᴜ ᴀʀᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ.
»`.ask` : ᴄʜᴀᴛ ɢᴘᴛ ᴀꜱᴋ ᴀɴʏ ᴛʜɪɴɢ.
»`.ping` : ᴄʜᴇᴄᴋ ꜱᴜᴘᴇʀʙᴀɴ ʙᴏᴛ ᴜᴘ ᴛᴏ ᴛɪᴍᴇ & ʟᴏᴀᴅ.
»`.id` : ᴅᴏ ᴜ ᴋɴᴏᴡ ᴡʜᴀᴛ ɪ.
»`.admin` : ʜᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ.
»`.tgm` : ɢᴇᴛ ɪᴍɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ.
»`.tr` : ᴛʀᴀɴꜱʟᴀᴛᴇ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ.
»`.joke` : ꜰᴏʀ ᴊᴏᴋᴇꜱ (ꜰᴜɴ)
»`.afk` : ᴀꜰᴋ ɪꜱ ᴀꜰᴋ ʟᴏʟ.
»`.song` : ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ ꜱᴏɴɢꜱ.
»`.video` : ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜱᴏɴɢꜱ.
»`.team` : ᴠɪᴇᴡ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ ᴍᴇᴍʙᴇʀꜱ
» ᴏᴛʜᴇʀ ᴄᴍᴅꜱ ᴍᴇɴᴜ ꜱᴏᴏɴ....
» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : `{pver}`
» ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{pyver()}
» ᴍʏ ᴏᴡɴᴇʀ : <a href=tg://user?id={OWNER_ID}>{m.from_user.first_name}</a>

» {Doneapped}
   ━━━━━━━━━━━━━━━━━━━""",
        )
    else:
        await m.reply_text("Profile picture not found.")

JOKE_API_ENDPOINT = 'https://hindi-jokes-api.onrender.com/jokes?api_key=1a6d440e3f5971eecebceee818c2'

@ass.on_message(filters.command(["joke"], prefixes=["."]) & filters.user(RAI))
async def joke(_, message):
    response = requests.get(JOKE_API_ENDPOINT)
    r = response.json()
    joke_text = r['jokeContent']
    await message.reply_text(joke_text)


@ass.on_message(filters.command(["team","members"], prefixes=["."]) & filters.user(RAI))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴛᴇᴀᴍ")
    await asyncio.sleep(2)
    await accha.edit("ꜱᴜᴘᴇʀʙᴀɴ")
    await asyncio.sleep(2)
    await accha.edit("ᴛᴇᴀᴍ ꨄ︎ ꜱᴜᴘᴇʀʙᴀɴ")
    await asyncio.sleep(2)
    await accha.delete()
    await asyncio.sleep(1)
    await m.reply_text("""
   ━━━━━━━━━━━━━━━━━━━
ʜᴇʀᴇ ɪꜱ ᴛᴇᴀᴍ ꜱᴜᴘᴇʀʙᴀɴ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴀᴅᴍɪɴꜱ :

1) @New_AMBOT (ꜰᴏᴜɴᴅᴇʀ)
2) @Sagar_11111111 (ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ)
3) @mdsuhelahmed (ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ)
4) @its_vikky_ydv (ᴀᴅᴍɪɴꜱ)
5) @Durgeshxi (ᴀᴅᴍɪɴꜱ)
6) @ll_raistar_ll (ᴀᴅᴍɪɴꜱ)
7) @fgdgdgdfg (ᴀᴅᴍɪɴꜱ)
8) @HLV_NARUTO_OP (ᴀᴅᴍɪɴꜱ)

» ᴘᴏᴡᴇʀ ʙʏ : @SpicyEmpire
   ━━━━━━━━━━━━━━━━━━━""")
