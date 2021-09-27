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

I am <b>Soleh Music.</b>

I can play music in your group.It will be fun!

Click /help for more details and command.

<b>✨Made by @sparkysunny✨.<b>
"""
HELP_TEXT = """
Help command 

/play - play a music!
/end - end the song!
/skip - skip a music!
/song - search a song!
"""
ABOUT_TEXT = """
⭕️<b>☢️My Name☢️: SolehMusic</b>

⭕️<b>☢️Developer:</b> <a href='https://t.me/sparkysunny/346'>Soleh</a>

⭕️<b>☢️My Group☢️ :</b> <a href='https://t.me/animefan_club777'>Anime Fan Club🌈🌈</a>

⭕️<b>☢️My channel☢️:</b> <a href='https://t.me/moviesebseriesAnimes'>Anime Gallery</a>
"""
"""

The bot is free to use and always will be!
But running this bot on server costs money, If you like this bot and want it to keep running, please support.

To donate you can choose any of these options and send any amount that you wish.
"""

START_BUTTONS = InlineKeyboardMarkup(
           [[
        InlineKeyboardButton('☢️Group☢️', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('☢️Channel☢️', url='https://t.me/moviesebseriesAnimes')
        ],[
        InlineKeyboardButton('☢️Feedback☢️', url='https://t.me/bussystudent/346'),
        InlineKeyboardButton('☢️Anime Wallpaper☢️', url='https://t.me/Todoroki_Shoto_777'),
        InlineKeyboardButton('☢️Music☢️', url='https://t.me/animefan_club777')
        ],[
        InlineKeyboardButton('☢️Subscribe to our CHANNEL☢️', url='https://t.me/moviesebseriesAnimes')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('☢️Group☢️', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('☢️Channel☢️', url='https://t.me/moviesebseriesAnimes')
        ],[
        InlineKeyboardButton('☢️Feedback☢️', url='https://t.me/bussystudent/346'),
        InlineKeyboardButton('☢️Anime Wallpaper☢️', url='https://t.me/Todoroki_Shoto_777'),
        InlineKeyboardButton('☢️Music☢️', url='https://t.me/animefan_club777')
        ],[
        InlineKeyboardButton('☢️Subscribe to our CHANNEL☢️', url='https://t.me/moviesebseriesAnimes')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
       [[
        InlineKeyboardButton('☢️Group☢️', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('☢️Channel☢️', url='https://t.me/moviesebseriesAnimes')
        ],[
        InlineKeyboardButton('☢️Feedback☢️', url='https://t.me/bussystudent/346'),
        InlineKeyboardButton('☢️Anime Wallpaper☢️', url='https://t.me/Todoroki_Shoto_777'),
        InlineKeyboardButton('☢️Music☢️', url='https://t.me/animefan_club777')
        ],[
        InlineKeyboardButton('☢️Subscribe to our CHANNEL☢️', url='https://t.me/moviesebseriesAnimes')
        ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton('☢️Group☢️', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('☢️Channel☢️', url='https://t.me/moviesebseriesAnimes')
        ],[
        InlineKeyboardButton('☢️Feedback☢️', url='https://t.me/bussystudent/346'),
        InlineKeyboardButton('☢️Anime Wallpaper☢️', url='https://t.me/Todoroki_Shoto_777'),
        InlineKeyboardButton('☢️Music☢️', url='https://t.me/animefan_club777')
        ],[
        InlineKeyboardButton('☢️Subscribe to our CHANNEL☢️', url='https://t.me/moviesebseriesAnimes')
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
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
    )

Deccan.run()
