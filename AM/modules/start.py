#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥
import random
from pyrogram import Client, filters
from config import BOT_USERNAME, CHANNEL, SUPPORT, OWNER_USERNAME, OWNER_ID
from AM import AM as ECOMUSIC 
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from AM.Helper.strings import (music_txt, ai_txt, bass_txt, youtube_txt, 
misc_txt, broadcast_txt, checker_txt, devs_txt, instagram_txt, fban)
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


# ------------------------------------------------------------------------------- #
AM_PIC = [
    "https://telegra.ph/file/7c25ef427c9f3cded5577.jpg",
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    "https://telegra.ph/file/1c62254d59baf7f968ba7.jpg",
    "https://telegra.ph/file/7a0553bd4664486ab3008.jpg",
    "https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg",
    "https://telegra.ph/file/2773dec98d87b8562618c.jpg",
    "https://telegra.ph/file/80353d02e0368b71d2666.jpg",
    "https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg",
    "https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg",
    "https://telegra.ph/file/8371bcd8952d089f9ec05.jpg",
    "https://telegra.ph/file/f970e559dd1bb96fced1a.jpg",
    "https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"
]
start_txt = """
**ʜᴇʟʟᴏ** {} 

ɪ ᴀᴍ 𝙀𝙘𝙤, ʏᴏᴜʀ ᴍᴜsɪᴄ ᴠɪʀᴛᴜᴏsᴏ! ɪᴍᴍᴇʀsᴇ ʏᴏᴜʀsᴇʟғ ɪɴ ғʟᴀᴡʟᴇss ʙᴇᴀᴛs ᴡɪᴛʜ ᴢᴇʀᴏ ʟᴀɢ – ɪ'ᴍ ɴᴏᴛ ᴊᴜsᴛ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ; ɪ'ᴍ ᴛʜᴇ sʏᴍᴘʜᴏɴʏ ᴏғ ᴛʜᴇ ғᴜᴛᴜʀᴇ, ᴛᴀɪʟᴏʀᴇᴅ ғᴏʀ ʏᴏᴜʀ ᴍᴜsɪᴄᴀʟ ʙʟɪss.

✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️
◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.
◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.
◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.
◆ ɴᴏ ᴘʀᴏᴍᴏ.
◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.
◆ ꜰᴜʟʟ ʙᴀꜱꜱ ʙᴏᴏᴍ ᴛᴏᴘ Qᴜᴀʟɪᴛʏ.
◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.
◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.
"""

# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),    
        ],
        [
            InlineKeyboardButton("ɢʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/{CHANNEL}"),    
        ],
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_"),    
        ]
])



# ------------------------------------------------------------------------------- #

help_txt = """**
**» 𝙀𝙘𝙤. ᴄᴏᴏʟ ᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs** 
"""



# ------------------------------------------------------------------------------- #

ECOMUSIC_buttons = [              
                [
                    InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="music_"),   
                    InlineKeyboardButton("ɢᴘᴛ-ᴀɪ", callback_data="ai_"),
                    InlineKeyboardButton("ʙᴀss", callback_data="bass_")
                ],
                [
                    InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ", callback_data="youtube_"),   
                    InlineKeyboardButton("ᴍɪsᴄ", callback_data="misc_"),
                    InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀsᴛ", callback_data="broadcast_")
                ],
                [
                    InlineKeyboardButton("ᴄʜᴇᴄᴋᴇʀ", callback_data="checker_"),   
                    InlineKeyboardButton("ᴅᴇᴠs", callback_data="devs_"),
                    InlineKeyboardButton("ɪɴsᴛᴀɢʀᴀᴍ", callback_data="instagram_")
                ],
               [
                     
                    InlineKeyboardButton("ꜱᴜᴘᴇʀꜰʙᴀɴ", callback_data="fban_"),

                ],
    
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]



#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥


@ECOMUSIC.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=start_txt.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )
    
@ECOMUSIC.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
            InlineKeyboardButton("ɢʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/{CHANNEL}"),    
        ],
            [
                InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention, query.from_user.id),
                reply_markup=reply_markup# Fix: Use query instead of message
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(ECOMUSIC_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="music_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                music_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="ai_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                ai_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="bass_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                bass_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="youtube_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                youtube_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="fban_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                fban,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    
        
    elif query.data=="misc_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                misc_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


        
    elif query.data=="broadcast_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                broadcast_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="checker_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                checker_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
    elif query.data=="devs_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                devs_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        



    elif query.data=="instagram_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                instagram_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

        
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

#┏━━━━━━━━━❥
#┣•Cʀᴇᴀᴛᴏʀ  ~ @New_AMBOT 
#┣•ᴜᴘᴅᴀᴛᴇꜱ1 ~ @AbhiModszYT_Return
#┣•ᴜᴘᴅᴀᴛᴇꜱ2 ~ @AMBOTYT
#┣•ᴘᴏᴡᴇʀ ʙʏ : @Logs_Gban
#┗━━━━━━━━━❥
