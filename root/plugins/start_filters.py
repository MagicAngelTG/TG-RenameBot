'''
RenameBot
Thanks to Spechide Unkle as always for the concept  ♥️
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from root.config import Config
from root.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("help"))
async def help_user(c,m):
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    button = [[
               InlineKeyboardButton("Update Channel", url=f"https://t.me/X_Botz"),
               InlineKeyboardButton("Support Group", url=f"https://t.me/X_Botzz")
               ],
               [
               InlineKeyboardButton("Developer", url=f"https://t.me/Akfronic"),
               InlineKeyboardButton("Share", url=f"https://t.me/share/url?url=Join%20%40X_Botz")
             ]]
    markup = InlineKeyboardMarkup(button) 
    try:
       await m.reply_text(Translation.START_TEXT,quote=True,reply_markup=markup,disable_web_page_preview=True) 
    except Exception as e:
        log.info(str(e))

        
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
