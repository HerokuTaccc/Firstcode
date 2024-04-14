import asyncio
import logging
import time
from pytgcalls import PyTgCalls
from importlib import import_module
from dotenv import load_dotenv
from pyrogram import Client
from config import (
     API_ID, 
     API_HASH,
     BOT_TOKEN, 
     SESSION_STRING,
     SuperFban,
     SuperFban1, 
     SuperFban2, 
     SuperFban4,
     SuperFban5,
     SuperFban6,
     SuperFban7,
     SuperFban3,
     SuperFban8,
     SuperFban9,
     SuperFban10,
     SuperFban11,
     SuperFban12,
)

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



AM = Client(
    name="SuperFban",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

userbot = Client(
    name="userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

fban = Client(
    name="fbanbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban,
)

fban1 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban1,
)

#fban2 = Client(
#    name="fbanbot1",
 #   api_id=API_ID,
  #   api_hash=API_HASH,
   # session_string=SuperFban2,
#)

fban3 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban3,
)

fban4 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban4,
)

fban5 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban5,
)

fban6 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban6,
)

fban7 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban7,
)


fban8 = Client(
    name="fbanbot1",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SuperFban8,
)
pytgcalls = PyTgCalls(userbot)



async def AM_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await AM.start()
    await userbot.start()
    await pytgcalls.start()
    await fban.start()
    await fban1.start()
  # await fban2.start()
    await fban3.start()
    await fban4.start()
    await fban5.start() 
    await fban6.start() 
    await fban7.start()
    await fban8.start()
    getme = await AM.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(AM_bot())
