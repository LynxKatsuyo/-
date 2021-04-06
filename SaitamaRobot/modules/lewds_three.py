import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

@run_async 
def wallpaper(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("wallpaper")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
    bot.send_document(chat_id = chat, document = nek, filename = "wall_generation", reply_to_message_id = user) 
   
@run_async 
def lewdk(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewdk")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def ngif(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("ngif")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def tickle(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("tickle")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def lewd(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewd")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def feed(update: Update, context: CallbackContext ):
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feed")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
  
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
LEWDK_HANDLER = DisableAbleCommandHandler("lewdk", lewd)
NGIF_HANDLER = DisableAbleCommandHandler("ngif", ngif)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)

dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(LEWDK_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(FEED_HANDLER)

