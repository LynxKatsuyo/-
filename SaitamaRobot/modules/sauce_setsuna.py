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
  sauce = SauceNao(api_key=API, db = 999, numres = 6)
  bot = context.bot 
  msg = update.effective_message 
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat 
  reply = msg.reply_to_message
  filename_photo = "saucey.png"
  filename_gif = "saucey.gif" 
  bot.send_chat_action(chat.id, action = 'typing')
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
  ru = []
  rsu_1  = ru.append(int(results[0].index_id)) 
  rsu_2 = ru.append(int(results[1].index_id))
  rsu_3 = ru.append(int(results[2].index_id))
  rsu_4 = ru.append(int(results[4].index_id))
  rsu_5 = ru.append(int(results[5].index_id))
  text = " "
  markup = " "
  tex_dan, url_dan, material_dan, creator_dan, source_dan, character_dan, tex_pix, mem_pix, url_pix,  anime_url, anime_title,  dan_simi, simi_pix, anime_year, anime_ep= " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "
  for i in ru:
    rsu, rsu2, rsu3, rsu4, rsu5 = " ", " ", " ", " ", " "
    if i == 9:
      rsudan = "True"
      rsu = int(ru.index(i)) 
    else:
      rsudan = "False"
    if i == 5:
      rsupix = "True"
      rsu2 = int(ru.index(i)) 
    else:
      rsupix = "False"
    if i == 21:
      rsuAnime = "True"
      rsu3 = int(ru.index(i)) 
    else:
      rsuAnime = "False"
    if i == 18:
      rsu_nhen = "True"
      rsu4 = int(ru.index(i)) 
    else:
      rsu_nhen = "False"
    if i == 22:
      rsu_hentai = "True"
      rsu5 = int(ru.index(i)) 
    else:
      rsu_hentai = "False"
      
  if rsudan == "True" :
    dan_simi = str(results[rsu].similarity)
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
    if not ik == "None":
      creator_dan = ik.get('creator') 
      material_dan = ik.get('material')
      source_dan = ik.get('source')
      character_dan = ik.get('characters')
    danboru = "True" 
  else:
    danboru = "False"
    
  if rsuAnime == "True":
    raww = results[rsu3].raw
    anime_url = results[rsu3].urls
    try:
      anime_url = anime_url[0]
    except IndexError:
      pass 
    simi = str(results[rsu3].similarity) 
    deta = raww.get('data')
    anime_title = deta.get('source') 
    anime_ep = deta.get('part')
    anime_year = deta.get('year')
    anime_timestamp = deta.get('est-time')
    anime = "True"
  else:
    anime = "False"
  
  if rsupix == "True" :
     url_pix = " ".join(results[rsu2].urls)
     if danboruu == "True":
       pass 
     if anime == "True":
       pass
     simi_pix = str(results[rsu2].similarity) 
     tex_pix = str(results[rsu2].title)
     kek = results[rsu2].raw
     ti = kek.get('data')
     if not ti == 'None':
       mem_pix = ti.get('member_name')
     pixiv = "True" 
  else:
     pixiv = "False"
  
  
  if anime == "True":
    text = f"*Title: {anime_title}\n    Episode: {anime_ep} \n    Year Released: {anime_year} \n     Timestamp: {anime_timestamp} *"
    
  if danboru == "True" :
    text = "*Title:*" + " " + f"*{tex_dan}*" + " " + "\n\n*Creator:*" + " " +  f"*{creator_dan}*" + "\n\n*Material:*" + " " + f" *{material_dan}*" + "\n\n*Character:*" + " " + f"*{character_dan}*" + " " + "*Similarity: " + " " + f"{dan_simi}*" 

  if pixiv == "True":
    if anime == "True":
      pass
    if danboru == "True":
      pass 
      text =  "*Title:*" + " " + f"*{tex_pix}*" + "\n\n" +  "*Artist:*" + " " + f"*{mem_pix}*" + f"'Similarity: {simi_pix}" 
  
  #if text == " ":
    #text = "Sorry Not found!!, Setsuna sad... reeeee"
  #buttons made here 
  keybo = []
  if pixiv == "True":
    keybo.append(InlineKeyboardButton(text = "Pixiv", url = url_pix))
  if danboru == "True":
    keybo.append(InlineKeyboardButton(text = "Danboru", url = url_dan))
  if anime == "True":
    keybo.append([InlineKeyboardButton(text = "Anime-db", url = anime_url)])
  markup = InlineKeyboardMarkup(inline_keyboard=keybo)
  bot.send_message(chat.id, text, reply_to_message_id = msg_id, reply_markup = markup, parse_mode = ParseMode.MARKDOWN)
   
     
  
SAUCE_HANDLER = DisableAbleCommandHandler("sauce", sauce) 
dispatcher.add_handler(SAUCE_HANDLER)
    
    
      