from saucenao_api import SauceNao 
from saucenao_api.params import DB

from SaitamaRobot.modules.disable import (DisableAbleCommandHandler, DisableAbleMessageHandler) 
from SaitamaRobot.modules.helper_funcs.chat_status import (user_admin,
                                                           user_not_admin)
from telegram import (Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      ParseMode, Update)
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          Filters, MessageHandler, run_async)
from telegram.utils.helpers import mention_html





API = "6851aa2ae17da0042a7b02af3f7a1c55485ceafc"
sauce = SauceNao(api_key=API, db = 999)



@run_async 
def sauce(update: Update, context: CallbackContext ):
  results = " "
  global sauce
  bot = context.bot 
  msg = update.effective_message 
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat 
  reply = msg.reply_to_message
  filename_photo = "saucey.png"
  filename_gif = "saucey.gif" 
  if reply:
    if reply.photo:
      photo_id = reply.photo.file_id
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
  rsu_1  = int(results[0].id) 
  rsu_2 = int(results[1].id)
  rsu_3 = int(results[2].id)
  text = " "
  tex_dan, url_dan, material_dan, creator_dan, source_dan, character_dan, tex_pix, mem_pix, url_pix = " "
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
    pass 
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
    pass
  if rsudan == "True" :
    tex_dan = str(results[rsu].title)
    urdan = results[rsu].urls
    tit = urdan.pop()
    url_dan = " ".join(urdan)
    creator_dan = " ".join(results[rsu].creator)
    material_dan = " ".join(results[rsu].material)
    source_dan = " ".join(results[rsu].source)
    character_dan = " ".join(results[rsu].character)
    danboruu = "True" 
  else:
     pass
  if rsupix == "True" :
     tex_pix = str(results[rsu2].title)
     url_pix = " ".join(results[rsu2].urls)
     mem_pix = " ".join(results[rsu2].member_name)
     pixiv = "True" 
  else:
     pass
  if danboruu == "True" :
    print("Danboruu hit!")
    text += f"[Danboruu]({url_dan}) + "\n" + "*Title*" + " " + tex_dan + "\n*Creator*" + " " +  creator_dan + "\n*Material*" + " " + material_dan + "\n*Character*" + " " + character_dan + \n*Source*" + " " + f"[Danboruu]({source_dan})" 
  else:
     print("Danboruu not found..")
  if pixiv == "True":
     if danboruu == "True":
      text += "Pixiv Url:" + " " + url_pix
    else:
      text += ("Source: Pixiv" + "\n" + "Title:" + " " + tex_pix + "\n" + "Url:" + " " + url_pix + "\n" +  "Artist:" + " " + mem_pix)
  bot.send_message(chat.id, text, reply_to_message_id = msg_id)
   
     
  
SAUCE_HANDLER = DisableAbleCommandHandler("sauce", sauce) 
dispatcher.add_handler(SAUCE_HANDLER)
    
    
      