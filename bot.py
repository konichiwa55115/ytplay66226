import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import shutil
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "playbot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5545470781:AAGjzXBuTOeJ1JulON1Cw0I2ZP8kebs2Alk"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أن بوت تحويل القنوات والقوائم إلى روابط\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  
  user_id = message.from_user.id 
  url = message.text
  
  message.reply_text("جار التحويل")
  cmd(f'yt-dlp --flat-playlist -i --print-to-file url links.txt {url}')
  with open('links.txt', 'r') as file:
      bot.send_document(message.chat.id, f)
  cmd(f'unlink links.txt')
bot.run()
