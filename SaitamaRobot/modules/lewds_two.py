import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

@run_async 
def sologif(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("solog")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def feet(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feet")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def feetgif(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feetg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def cumgif(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("cumg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def erokemo(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("erokemo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def lesbian(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("les")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
  
SOLOGIF_HANDLER = DisableAbleCommandHandler("sologif", sologif)
FEET_HANDLER = DisableAbleCommandHandler("feet", feet)
FEETGIF_HANDLER = DisableAbleCommandHandler("feetgif", feetgif)
CUMGIF_HANDLER = DisableAbleCommandHandler("cumgif", cumgif)
EROKEMO_HANDLER = DisableAbleCommandHandler("erokemo", erokemo)
LESBIAN_HANDLER = DisableAbleCommandHandler("lesbian", lesbian)

dispatcher.add_handler(SOLOGIF_HANDLER)
dispatcher.add_handler(FEET_HANDLER)
dispatcher.add_handler(FEETGIF_HANDLER)
dispatcher.add_handler(CUMGIF_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)

