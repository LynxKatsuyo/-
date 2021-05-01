from saucenao_api import SauceNao 
from saucenao_api.params import DB
import os
from SaitamaRobot import dispatcher 
from SaitamaRobot.modules.disable import (DisableAbleCommandHandler, DisableAbleMessageHandler) 
from SaitamaRobot.modules.helper_funcs.chat_status import (user_admin,
                                                           user_not_admin)
from telegram import (Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      ParseMode, Update)
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          Filters, MessageHandler, run_async)
from telegram.utils.helpers import mention_html








@run_async 
def sauce(update: Update, context: CallbackContext ):
  results = " "
  API = "6851aa2ae17da0042a7b02af3f7a1c55485ceafc"
  sauce = SauceNao(api_key=API, db = 999)
  bot = context.bot 
  msg = update.effective_message 
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat 
  reply = msg.reply_to_message
  filename_photo = "saucey.png"
  filename_gif = "saucey.gif" 
  if not reply:
    bot.send_message(chat.id, "Reply to something baka...")
    return
  if reply:
    if reply.photo:
      photo_id = reply.photo[-1].file_id
      photo = "True" 
    elif reply.animation:
      gif_id = reply.animation.file_id
      gif = "True" 
    elif reply.sticker:
      photo_id = reply.sticker.file_id
      photo = "True" 
    else:
      bot.send_message(chat_id = chat, text = "Nyah!!, give a gif, photo or a sticker!! ", reply_to_message_id = msg_id)
      return
    if photo == "True":
      file = bot.get_file(photo_id)
      dl = file.download(filename_photo)
      oo = open(dl, 'rb')
      results = sauce.from_file(oo)
    elif gif == "True" :
      file = bot.get_file(gif_id)
      dl = file.download(filename_gif)
      oo = open(dl, 'rb')
      results = sauce.from_file(oo)
    else:
      return
  rsu_1  = int(results[0].index_id) 
  rsu_2 = int(results[1].index_id)
  rsu_3 = int(results[2].index_id)
  text = " "
  markup = " "
  tex_dan, url_dan, material_dan, creator_dan, source_dan, character_dan, tex_pix, mem_pix, url_pix = " ", " ", " ", " ", " ", " ", " ", " ", " "
  if rsu_1 == 9:
    rsudan = "True" 
    rsu = 0 
  elif rsu_2 == 9:
    rsudan = "True" 
    rsu = 1
  elif rsu_3 == 9:
    rsudan = "True"  
    rsu = 2
  else:
    rsudan = "False"
  if rsu_1 == 5:
    rsupix = "True" 
    rsu2 = 0
  elif rsu_2 == 5:
    rsupix = "True"  
    rsu2 = 1 
  elif rsu_3 == 5:
    rsupix ="True" 
    rsu2 = 2 
  else:
    rsupix = "False"
  if rsudan == "True" :
    tex_dan = str(results[rsu].title)
    urdan = results[rsu].urls
    try:
      urgel = urdan[1]
    except IndexError:
      pass
    tit = urdan.pop()
    url_dan = " ".join(urdan)
    di = results[rsu].raw
    ik = di.get('data')
    if not data == "None":
      creator_dan = ik.get('creator') 
      material_dan = ik.get('material')
      source_dan = ik.get('source')
      character_dan = ik.get('characters')
      danboruu = "True" 
  else:
    danboruu = "False"
  if rsupix == "True" :
     tex_pix = str(results[rsu2].title)
     url_pix = " ".join(results[rsu2].urls)
     kek = results[rsu2].raw
     ti = kek.get('data')
     if not ti == 'data':
       mem_pix = ti.get(member_name)
     pixiv = "True" 
  else:
     pass
  if danboruu == "True" :
    text += "*Title:*" + " " + tex_dan + " " + "\n*Creator:*" + " " +  creator_dan + "\n*Material:*" + " " + material_dan + "\n*Character:*" + " " + character_dan  + " "
  else:
     print("Danboruu not found..")
  if pixiv == "True":
     if danboruu == "True":
      text += f"[Pixiv Url]({url_pix})" 
     else:
      text += ("Source: Pixiv" + "\n" + "Title:" + " " + tex_pix + "\n" + f"[Url]({url_pix})" + "\n" +  "Artist:" + " " + mem_pix)
  #buttons made here 
  if pixiv == "True":
    url1 = url_pix
    url1_name = "Pixiv"
  elif danboruu == "True":
    url1 = url_dan
    url1_name = "Danboruu"
  if url1_name == "Pixiv":
    url2 = url_dan
    url2_name = "Danboruu"
  markup = InlineKeyboardMarkup([[InlineKeyboardButton(text = f"{url1_name}", url = f"{url1}")], [InlineKeyboardButton(text = f"{url2_name}", url = f" {url2}")]])
  bot.send_message(chat.id, text, reply_to_message_id = msg_id, reply_markup = markup, parse_mode = ParseMode.MARKDOWN)
   
     
  
SAUCE_HANDLER = DisableAbleCommandHandler("sauce", sauce) 
dispatcher.add_handler(SAUCE_HANDLER)
    
    
      