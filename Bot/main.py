from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Bot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import bot as app
from Bot import LOGGER

pm_start_text = """
හේ හේ හිච්චි පුතේ 😇 \n\n දන්නවනේ ඉතින්. මම තමයි අපේ නිපුන් කොලුවගෙ ඇසිස්ටන්ට්.. ඌ දැන් පට්ට බිසී 😅 \n ඉස්සර වගේ නෙවේනෙ පුතේ දැන් වගකීම් එහෙමත් වැඩිනෙ ඒකාට 😅 \n\n ඉතින් පුතේ ඔය හෙල්ප් බටන් එක එබුවම විස්තරේ එයි 😇 ගහලම බලපම්කෝ.. \n\n එහෙනම් හිච්චි පුතේ අපි කැපුනා 🥸
"""

help_text = """
ඔන්න පුතේ කමාන්ඩ්ස් ටික👇
- /song 
- /saavn 
- /deezer 
- 
මරු හැබැයි 😎
"""

about_text = """
ඔන්න පුතේ කමාන්ඩ්ස් ටික👇
- /song 
- /saavn 
- /deezer 
- 
මරු හැබැයි 😎
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝑯𝒆𝒍𝒑", callback_data="help_text"
                    ),
                    InlineKeyboardButton(
                        text="𝑰𝒏𝒃𝒐𝒙", url="https://t.me/NiupunDinujaya"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)
    
@app.on_message(filters.command("about"))
async def start(client, message):
    await message.reply(about_text)

app.start()
LOGGER.info("බොටා වැඩ පුතේ.")
idle()
