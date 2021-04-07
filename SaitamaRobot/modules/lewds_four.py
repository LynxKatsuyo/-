import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

@run_async 
def eronyuri(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("eroyuri")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def eron(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("eron")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def cumpic(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("cumpic")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def bj(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("bj")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def nekonsfw(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("nekonsfw")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def solo(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("solo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
  
ERONYURI_HANDLER = DisableAbleCommandHandler("eronyuri", eronyuri)
ERON_HANDLER = DisableAbleCommandHandler("eron", eron)
CUMPIC_HANDLER = DisableAbleCommandHandler("cumpic", cumpic)
BJ_HANDLER = DisableAbleCommandHandler("bj", bj) 
NEKONSFW_HANDLER = DisableAbleCommandHandler("nekonsfw", nekonsfw)
SOLO_HANDLER = DisableAbleCommandHandler("solo", solo )

dispatcher.add_handler(ERONYURI_HANDLER)
dispatcher.add_handler(ERON_HANDLER)
dispatcher.add_handler(CUMPIC_HANDLER)
dispatcher.add_handler(BJ_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(SOLO_HANDLER)

