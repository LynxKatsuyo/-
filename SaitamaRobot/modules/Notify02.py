import html

from SaitamaRobot.modules.disable import (DisableAbleCommandHandler, DisableAbleMessageHandler) 
from SaitamaRobot import (LOGGER, DRAGONS, TIGERS, WOLVES, dispatcher)
from SaitamaRobot.modules.helper_funcs.chat_status import (user_admin,
                                                           user_not_admin)
from SaitamaRobot.modules.log_channel import loggable
from SaitamaRobot.modules.sql import reporting_sql as sql
from telegram import (Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      ParseMode, Update)
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          Filters, MessageHandler, run_async)
from telegram.utils.helpers import mention_html

NOTIF_GROUP = 12
REPORT_IMMUNE_USERS = DRAGONS + TIGERS + WOLVES

@run_async 
def req(update: Update, context: CallbackContext):
  bot = context.bot 
  message =update.effective_message
  ms = message.reply_to_message
  user = update.effective_user 
  chat = update.effective_chat 
  message_id = update.effective_message.message_id
  if message.text.startswith("/req"):
    pass
  elif message.text.split(None, 1)[0] = "#req":
    pass
  else:
    print("Called by # but was not #req")
    return
  if message.reply_to_message:
    argue = message.reply_to_message.text.split(None, 1)
  else:
    argue = message.text.split(None, 1)
  if len(argue) >= 2:
    args = argue[1]
  else:
    args = "None"
  
  if chat and sql.chat_should_report(chat.id):
        if ms:
          requesting_user = ms.from_user
        else:
          requesting_user = user.id
        chat_name = chat.title or chat.first or chat.username
        admin_list = chat.get_administrators()
        message = update.effective_message

        if args == "None":
            message.reply_text("Nyah boi request something!!")
            return "" 
        if chat and chat.type == Chat.SUPERGROUP:
          requested = "Nyahh!! Request accepted!!" 
          msg = f"<b>Request: </b>{html.escape(chat.title)}\n<b>Requested: </b> {args}\n<b>Requesting User:</b> {mention_html(user.id, user.first_name)}"
          link = link = f'<b> • The message:</b> <a href="https://t.me/{chat.username}/{message.message_id}">click here</a>'
        for admin in admin_list:
          if admin.user.is_bot:
            #ignore bots
            continue
          if sql.user_should_report(admin.user.id):
            try:
              if not chat.type == Chat.SUPERGROUP:
                        bot.send_message(
                            admin.user.id,
                            msg + link,
                            parse_mode=ParseMode.HTML)
                            
              if not chat.username:
                bot.send_message(admin.user.id, msg + link, parse_mode=ParseMode.HTML)

              if chat.username and chat.type == Chat.SUPERGROUP:
                        bot.send_message(
                            admin.user.id,
                            msg + link,
                            parse_mode=ParseMode.HTML)

            except Unauthorized:
              pass
            except BadRequest as excp:  # TODO: cleanup exceptions
              LOGGER.exception("Exception while reporting user")

        message.reply_text("Nyah! Request Accepted!!") 
        return msg

        return ""  
  
REQU_HANDLER = DisableAbleCommandHandler ("request", req) 
REQ_HANDLER = DisableAbleMessageHandler(Filters.regex(r"^#[^\s]+"), req, friendly="request")
 
dispatcher.add_handler(REQU_HANDLER, NOTIF_GROUP)
dispatcher.add_handler(REQ_HANDLER, NOTIF_GROUP)
            
          
