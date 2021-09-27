import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Hello {}, 
I am <b>Todoroki Music.</b>

I can play music in your group. . .

Click /help for more details..

<b>✨Made by @Mochi875 and @Shoto_GirlFriend_777✨.<b>
"""
HELP_TEXT = """
Help command 

/play - play a music
/end - end
/skip - skip a music
/song - search a song

"""
ABOUT_TEXT = """
⭕️<b>My Name💖: Todoroki Shoto</b>

⭕️<b>Worker💖:</b> <a href='https://t.me/sparkysunny/346'>Soleh</a>

⭕️<b>My Group💖 :</b> <a href='https://t.me/animefan_club777'>Anime Fan Club🌈🌈</a>

⭕️<b>My channel💖 :</b> <a href='https://t.me/moviesebseriesAnimes'>Anime Gallery</a>
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('My Group💖', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('My channel💖', url='https://t.me/moviesebseriesAnimes')
        ],[
        InlineKeyboardButton('Feedback', url='https://t.me/bussystudent/346'),
        InlineKeyboardButton('Anime Wallpaper', url='https://t.me/Todoroki_Shoto_777'),
        InlineKeyboardButton('Music🎤', url='https://t.me/animefan_club777')
        ],[
        InlineKeyboardButton('🌈Subscribe to our Channel🌈', url='https://t.me/moviesebseriesAnimes')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await update.reply_text(
        text=DONATE_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=DONATE_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )

 message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

Deccan.run()
