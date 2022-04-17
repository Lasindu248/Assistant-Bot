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

START_STICKER = "CAACAgIAAxkBAAEIpNJiWuv1eyICxhrO5S4rW1GtPlgzhAAChBgAAup12UryWtFUKpG2fyQE"

HELP_STICKER = "CAACAgIAAxkBAAEIpNViWuwery3UKAP_XoGcSKD3mwbcmgAC1BgAAn-z2UosweD7BFw4eCQE"

ABOUT_STICKER = "CAACAgIAAxkBAAEIpNpiWuxBIHXtQ22oeh1XaAJRbKEb7QACqhgAAiyP2UoUvDplq4VrLyQE"

CONTACT_STICKER = ""

WEBSITE_STICKER = "https://telegra.ph/file/1bd95dd19b2e858a90cb0.jpg"

SOCIAL_STICKER = "CAACAgIAAxkBAAEIpOFiWuySGJ3VxPQIBL3kmefEMiYI8QACKxYAAlRp2EoLdzJgp83IySQE"

GITHUB_STICKER = "CAACAgIAAxkBAAEIpN5iWuxxrXt-_maPh0fXg1oudS2tjwACXxkAAtd62UqfuXfbINkg3yQE"

CREDITS_STICKER = "CAACAgIAAxkBAAEIpORiWuytpRF-UfoUPpnCdJF4gcRONgACzxoAAnnx2Upvza882mbpIiQE"

SUPPORT_STICKER = ""

START_TEXT = """
හේ හේ හිච්චි පුතේ 😇
දන්නවනේ ඉතින්. මම තමයි අපේ නිපුන් කොලුවගෙ ඇසිස්ටන්ට්.. ඌ දැන් පට්ට බිසී 😅 
ඉස්සර වගේ නෙවේනෙ පුතේ දැන් වගකීම් එහෙමත් වැඩිනෙ ඒකාට 😅 
ඉතින් පුතේ ඔය හෙල්ප් බටන් එක එබුවම විස්තරේ එයි 😇 ගහලම බලපම්කෝ.. 
එහෙනම් හිච්චි පුතේ අපි කැපුනා 🥸
"""

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

ABOUT_TEXT = """
ස්ටාර්ට් ටෙක්ස්ට් එකේ තිබ්බ වගේ මේක තමයි පුතෙ නිපුන් කොලුවගෙ ඇසිස්ටන්ට් 😇 \n\n නිපුන්ව කන්ටැක්ට් කරගන්න හැටි , සෝසල් මීඩියා , ගිට්හබ් ප්‍රොෆයිල් එක වගේ ඔක්කොම මේ බොටාගෙ තීනව 🤓 \n\n තව එකක් හිච්චි පුතේ නිපුන් & ලසිඳු ඒ කියන්නෙ @NiupunDinujaya @LasiduOfficial කියන්නෙ එක්කෙනෙක් 😇 \n\n උගෙ ඇත්ත නම ලසිඳු .. \n\n නම වෙනස් කරගෙන ඉන්නෙ ඇයි කියල ඌවත් දන්නෑලු \n\n\n පිස්සු නේතෙ   
"""

CONTACT_TEXT = """
හිච්චි පුතේ නිපුන් කොලුව පොඩ්ඩක් බිසී මේ දවස් වල 🥲 \n\n ඉතින් @NiupunDinujaya ඉන්බොක්ස් ගිහිල්ල කන්ටැක්ට් කරගනිම් 🙂 \n\n රිප්ලයි කරන්න පරක්කු උනා කියල උගෙ ලොකුකම දැන් කියල හිතන්න එපා හිච්චි පුතේ 🥰 \n\n එහෙනම් කොල්ලො මැසේජ් එකක් දාලා වරෙම් 🥸
"""

WEBSITE_TEXT = """
හේ හේ හිච්චි පුතේ නිපුන් කොලුව වෙබ්සිටෙ එක හැදුවෙ PHP වලින් 😎 \n\n එකෙ උගෙ එක එක ප්‍රොජෙක්ට් තීනව බර්ත්ඩේ ගිෆ්ට් , ප්‍රශ්නවට වගේ .. යට තීන බටන් වලින් ගිහිල්ලම බලාම්කො
"""

SOCIAL_TEXT = """
හිච්චි පුතේ අපේ එකාගෙ ඔක්කොම වෙබ්සයිට් යට තීන බටන් එකේ තීන වෙබ්සයිට් එකෙන් ගන්න පුලුවන් 😎 \n ගිහිල්ලම බලාම්කො... \n\n\n බලහම් ඉතින් 😎
"""

GITHUB_TEXT = """
හේ හේ හිච්චි පුතේ ඔය තීන්නෙ ප්‍රොජෙක්ට් ටිකක් එක්ක නිපුන් කොලුවගෙ ගිටහබ් ප්‍රොෆයිල් එක 😎 
"""

CREDITS_TEXT = """
හිච්චි පුතේ මේ අහපන් .. මේ බොටාගෙ කෝඩ් එක ලිව්වෙ මම නෙවේ. අපේ මිස්ටර් දමන්ත අයියා.. ඉතිම් බොටාගෙ ඔක්කොම ක්‍රෙඩිට්ස් යන්නෙ අපේ දමන්ත කොලුවට.. 
"""

SUPPORT_TEXT = """
හිච්චි පුතේ මේ අහපන් .. උබලට මට උදව්වක් කරගෙන යන්නත් පුලුවන්.. හේ හේ ඉතිම් දන්නවනේ. ගෑස් නෑ හාල් නෑ තෙල් නෑ ඉතිම් කොලුවෝ ඉන්බොක්ස් ඇවිල්ලා විස්තරේ අහගෙන කීයක් හරි දීල පලයම් ඈ 😎 \n\n ඔය RDP , VPS , TG Acc උනත් කමක් නෑ 😎
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑹𝒆𝒑𝒐', url='https://github.com/Lasindu248/Assistant-Bot'),
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙',url='https://t.me/NiupunDinujaya')
        ]]
)


HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('𝑹𝒆𝒑𝒐',url='https://github.com/Lasindu248/Assistant-Bot')
        ]]
)

CONTACT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya')
        ]]
)

ABOUT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='http://t.me/NiupunDinujaya')
        ]]
)

WEBSITE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑺𝒐𝒄𝒊𝒂𝒍 𝑴𝒆𝒅𝒊𝒂', url='https://www.lasindu.ml/social.php'),
        InlineKeyboardButton('𝑯𝒂𝒑𝒑𝒚 𝑩𝒊𝒓𝒕𝒉𝒅𝒂𝒚',url='https://www.lasindu.ml/hbd.php')
        ],
        [
        InlineKeyboardButton('𝑲𝒏𝒐𝒘𝒅𝒍𝒂𝒈𝒆', url='https://www.lasindu.ml/quiz.php'),
        InlineKeyboardButton('𝑪𝒐𝒗𝒊𝒅',url='https://www.lasindu.ml/covid.php)
        ]]
)
            
SOCIAL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑺𝒐𝒄𝒊𝒂𝒍 𝑴𝒆𝒅𝒊𝒂', url='https://www.lasindu.ml/social.php')
        ]]
)
            
GITHUB_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑮𝒊𝒕𝒉𝒖𝒃', url='https://github.com/Lasindu248')
        ]]
)
            
CREDITS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑫𝒂𝒎𝒂𝒏𝒕𝒉𝒂 𝑱𝒂𝒔𝒊𝒏𝒈𝒉𝒆', url='https://t.me/MrItzme'),
        InlineKeyboardButton('𝑮𝒊𝒕𝒉𝒖𝒃', url='https://github.com/Damantha126')
        ]]
)
          
SUPPORT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('𝑰𝒏𝒃𝒐𝒙', url='https://t.me/NiupunDinujaya')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        START_STICKER,
        caption=START_TEXT,
        reply_markup=START_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)
        
@KINGAMDA.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_photo(
        HELP_STICKER,
        caption=HELP_TEXT,
        reply_markup=HELP_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)   
    
@KINGAMDA.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_photo(
        ABOUT_STICKER,
        caption=ABOUT_TEXT,
        reply_markup=ABOUT_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
) 
    
@KINGAMDA.on_message(filters.private & filters.command(["social"]))
async def start(bot, update):
    await update.reply_photo(
        SOCIAL_STICKER,
        caption=SOCIAL_TEXT,
        reply_markup=SOCIAL_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
) 

@KINGAMDA.on_message(filters.private & filters.command(["github"]))
async def start(bot, update):
    await update.reply_photo(
        GITHUB_STICKER,
        caption=GITHUB_TEXT,
        reply_markup=GITHUB_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
) 
            
@KINGAMDA.on_message(filters.private & filters.command(["website"]))
async def start(bot, update):
    await update.reply_photo(
        WEBSITE_STICKER,
        caption=WEBSITE_TEXT,
        reply_markup=WEBSITE_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
) 
            
@KINGAMDA.on_message(filters.private & filters.command(["contact"]))
async def start(bot, update):
    await update.reply_photo(
        CONTACT_STICKER,
        caption=CONTACT_TEXT,
        reply_markup=CONTACT_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
) 
            
@KINGAMDA.on_message(filters.private & filters.command(["credits"]))
async def start(bot, update):
    await update.reply_photo(
        CREDITS_STICKER,
        caption=CREDITS_TEXT,
        reply_markup=CREDITS_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)
            
@KINGAMDA.on_message(filters.private & filters.command(["supportme"]))
async def start(bot, update):
    await update.reply_photo(
        SUPPORT_STICKER,
        caption=SUPPORT_TEXT,
        reply_markup=SUPPORT_BUTTON,
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)

            
            
KINGAMDA.run()  
