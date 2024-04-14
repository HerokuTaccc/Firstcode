import pydub
from AM import AM as ECOMUSIC
from pyrogram import filters


#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥
@ECOMUSIC.on_message(filters.command("bass") & filters.reply)
async def download_and_enhance_audio(client, message):
    try:
        reply_message = message.reply_to_message

        if reply_message.audio:
            msg = await message.reply("processing")
            audio = await reply_message.download()
            audio_segment = pydub.AudioSegment.from_file(audio)
            await msg.edit("now adding bass and uploading...")
            
            enhanced_audio = audio_segment + 10           
            enhanced_audio.export("ECOMUSIC.mp3", format="mp3")
            await msg.delete()
            await message.reply_audio("ECOMUSIC.mp3")
        else:
            await message.reply("The replied message is not an audio.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")



#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥

@ECOMUSIC.on_message(filters.command("loudly") & filters.reply)
async def download_and_enhance_audio(client, message):
    try:
        reply_message = message.reply_to_message

        if reply_message.audio:
            msg = await message.reply("processing")
            audio = await reply_message.download()
            audio_segment = pydub.AudioSegment.from_file(audio)
            await msg.edit("now adding loude audio and uploading...")
        
            louder_audio = audio_segment + 10
            
            louder_audio.export("ECOMUSIC.mp3", format="mp3")
            await msg.delete()
            await message.reply_audio("ECOMUSIC.mp3")
        else:
            await message.reply("The replied message is not an audio.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥



@ECOMUSIC.on_message(filters.command("mono") & filters.reply)
async def split_stereo_and_send_audio(client, message):
    try:
        reply_message = message.reply_to_message

        if reply_message.audio:
            msg = await message.reply("processing")
            a = pydub.AudioSegment.from_file(await reply_message.download())
            b = a.split_to_mono()
            mono_audio = b[0]
            await msg.edit("now adding mono audio and uploading...")
            
            mono_audio.export("ECOMUSIC.mp3", format="mp3")
            await msg.delete()
            await message.reply_audio("ECOMUSIC.mp3")
        else:
            await message.reply("The replied message is not an audio.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")


              
#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥
