import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

@run_async
async def neko(update: Update, context: CallbackContext ):
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat
    nek = nekos.img("neko")
    await bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
  
NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
dispatcher.add_handler(NEKO_HANDLER)





