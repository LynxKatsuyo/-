import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

@run_async 
def neko(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("neko")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def yuri(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("yuri")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def trap(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("trap")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def futanari(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("futanari")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def hololewd(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("hololewd")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def lewdkemo(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewdkemo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
  
NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
YURI_HANDLER = DisableAbleCommandHandler("yuri", yuri)
TRAP_HANDLER = DisableAbleCommandHandler("trap", trap)
FUTANARI_HANDLER = DisableAbleCommandHandler("futanari", futanari)
HOLOLEWD_HANDLER = DisableAbleCommandHandler("hololewd", hololewd)
LEWDKEMO_HANDLER = DisableAbleCommandHandler("lewdkemo", lewdkemo )

dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(YURI_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(FUTANARI_HANDLER)
dispatcher.add_handler(HOLOLEWD_HANDLER)
dispatcher.add_handler(LEWDKEMO_HANDLER)

