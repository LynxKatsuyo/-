import datetime
import codecs
import html
import os
import random
import re
import subprocess
import requests as r
from SaitamaRobot import dispatcher 

from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown, mention_html
from telegram import (
    Chat,
    ChatAction,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
    ParseMode,
    TelegramError,
)




@run_async
def rmemes(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    context.bot.send_chat_action(chat.id, action="upload_photo")

    SUBREDS = [
        "Animemes"
        "hentaimemes"
        "meirl",
        "dankmemes",
        "AdviceAnimals",
        "memes",
        "meme",
        "memes_of_the_dank",
        "PornhubComments",
        "teenagers",
        "memesIRL",
        "insanepeoplefacebook",
        "terriblefacebookmemes",
    ]

    subreddit = random.choice(SUBREDS)
    res = r.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}")

    if res.status_code != 200:  # Like if api is down?
        msg.reply_text("Sorry some error occurred :(, possibly api is down")
        return
    else:
        res = res.json()

    rpage = res.get(str("subreddit"))  # Subreddit
    title = res.get(str("title"))  # Post title
    memeu = res.get(str("url"))  # meme pic url
    plink = res.get(str("postLink"))

    caps = f"× <b>Title</b>: {title}\n"
    caps += f"× <b>Subreddit:</b> <pre>r/{rpage}</pre>"

    keyb = [[InlineKeyboardButton(text="Postlink 🔗", url=plink)]]
    try:
        context.bot.send_photo(
            chat.id,
            photo=memeu,
            caption=(caps),
            reply_markup=InlineKeyboardMarkup(keyb),
            timeout=60,
            parse_mode=ParseMode.HTML,
        )

    except BadRequest as excp:
        return msg.reply_text(f"Error! {excp.message}")
       

__help__ = """
***Rmeme Module**

`/rmeme`: Try it urself baka! 

""" 
R_HANDLER = CommandHandler("rmeme", rmemes)
dispatcher.add_handler(R_HANDLER)

__mod_name__ = "Rmeme"
