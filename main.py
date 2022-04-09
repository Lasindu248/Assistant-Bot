import os
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KINGAMDA = Client(
    "king-amda",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_IMG = "https://telegra.ph/file/6a277e0bb77d5c5e87666.jpg"

START_TEXT = """
හේ හේ හිච්චි පුතේ 😇
දන්නවනේ ඉතින්. මම තමයි අපේ නිපුන් කොලුවගෙ ඇසිස්ටන්ට්.. ඌ දැන් පට්ට බිසී 😅 
ඉස්සර වගේ නෙවේනෙ පුතේ දැන් වගකීම් එහෙමත් වැඩිනෙ ඒකාට 😅 
ඉතින් පුතේ ඔය හෙල්ප් බටන් එක එබුවම විස්තරේ එයි 😇 ගහලම බලපම්කෝ.. 
එහෙනම් හිච්චි පුතේ අපි කැපුනා 🥸
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑯𝒆𝒍𝒑', callback_data='HELP_TEXT'),
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙',url='https://t.me/NiupunDinujaya')
        ]]
)


HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑩𝒂𝒄𝒌', callback_data='START_TEXT'),
        InlineKeyboardButton('𝑹𝒆𝒑𝒐',url='https://github.com/Lasindu248/Assistant-Bot')
        ]]
)

HELP_TEXT = """
පුතේ මේ තීන්නෙ කමාන්ඩ්ස් ටික 👇

/help
/about
/contact
/website
/social
/github

හේ හේ මරු හැබැයි 😎
"""

HELP_IMG = "https://telegra.ph/file/50d549faaddb997964d38.jpg"

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(START_IMG)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
)
        
@KINGAMDA.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_photo(HELP_IMG)
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        
)    

KINGAMDA.run()  
