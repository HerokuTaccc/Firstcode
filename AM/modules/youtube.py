import os
import asyncio
import requests
import wget
import yt_dlp
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pyrogram import filters
from pyrogram.types import *
from AM import AM as ECOMUSIC
from AM import fban4 as app, fban3 as ass, fban5 as dur, fban as ambot
from config import OWNER_ID, FBAN, UNFBAN, SUDO_USERS, APPEND, Doneapped

sagar = 6634748952
vick = 7147100550
Durgesh = 6601999645

@ambot.on_message(filters.command(["video"], prefixes=["."]) & filters.user(OWNER_ID))
@dur.on_message(filters.command(["video"], prefixes=["."]) & filters.user(Durgesh))
@ass.on_message(filters.command(["video"], prefixes=["."]) & filters.user(vick))
@app.on_message(filters.command(["video"], prefixes=["."]) & filters.user(sagar))
@ECOMUSIC.on_message(filters.command("video"))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**ᴠɪᴅᴇᴏ ᴘʀᴏᴄᴇss.**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Error:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("**ᴘʀᴏᴄᴇss ᴄᴏᴍᴘʟᴇᴛᴇᴅ.\n ɴᴏᴡ ᴜᴘʟᴏᴀᴅɪɴɢ.**")
    title = ytdl_data["title"]
    await message.reply_video(file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"{title}\n**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ {message.from_user.mention}**")
     
    await msg.delete()
    try:
        os.remove(file_name)
    except Exception as e:
        print(e)                                  

flex = {}
chat_watcher_group = 3

                       
ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}  

# ------------------------------------------------------------------------------- #
@ambot.on_message(filters.command(["song"], prefixes=["."]) & filters.user(OWNER_ID))
@dur.on_message(filters.command(["song"], prefixes=["."]) & filters.user(Durgesh))
@ass.on_message(filters.command(["song"], prefixes=["."]) & filters.user(vick))
@app.on_message(filters.command(["song"], prefixes=["."]) & filters.user(sagar))
@ECOMUSIC.on_message(filters.command("song"))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔄 sᴇᴀʀᴄʜɪɴɢ... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("**⚠️ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴛʏᴘᴇᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ sᴏɴɢ ɴᴀᴍᴇ**")
        print(str(e))
        return
    m.edit("**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**📤 ᴜᴘʟᴏᴀᴅɪɴɢ...**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\n**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ {message.from_user.mention}**",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

# ------------------------------------------------------------------------------- #

#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥
