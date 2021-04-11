import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

SAYON = ['on', 'yes', 'On', 'ON', 'Yes', 'YES']
SAYNO = ['no', 'No', 'NO', 'OFF', 'Off', 'off']

@run_async 
def nsfw(update: Update, context: CallbackContext ):
  NSFW = True
  bot = context.bot
  msg = update.effective_message.text.split(" ", 1)
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat.id 
  if len(msg) >= 2:
    args = msg[1]
  else:
    ItsTime = True
  if args in SAYON:
    Status = "On!!"
    NSFW = True
    bot.send_message(chat_id = chat, text = "Feelings intensifies as NSFW is allowed!! Nyah!!", reply_to_message_id = msg_id)
  elif args in SAYNO:
    Status = "Off!!"
    NSFW = False
    bot.send_message(chat_id = chat, text = "Uhk Nsfw isn't allowed in this chat now.. Mewo!!", reply_to_message_id= msg_id )
  else:
    bot.send_message(chat_id = chat, text = "Baka!!, Give me on/off or yes/no so that i can manage nsfw control.. Meow!! ", reply_to_message_id = msg_id )
  if ItsTime == True:
    bot.send_message(chat_id = chat, text = "Nsfw in this chat is {}.format(Status)", reply_to_message_id = msg_id )
  else:
    pass
  
@run_async 
def neko(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("neko")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def yuri(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("yuri")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def trap(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("trap")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def futanari(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("futanari")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def hololewd(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("hololewd")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def lewdkemo(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewdkemo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def sologif(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("solog")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def feet(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feet")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def feetgif(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feetg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def cumgif(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("cumg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def erokemo(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("erokemo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async
def lesbian(update: Update, context: CallbackContext):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("les")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def wallpaper(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("wallpaper")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def lewdk(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewdk")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def ngif(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("ngif")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def tickle(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("tickle")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def lewd(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("lewd")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def feed(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("feed")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def kemonomimi(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("kemonomimi")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def gasm(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("gasm")
    r = requests.get(nek)
    o = open(r, "rb")
    bot.send_sticker(chat_id = chat, sticker = o, reply_to_message_id = user)

@run_async 
def poke(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("poke")
    bot.send_animation(chat_id = chat, animation= nek, reply_to_message_id = user)
      
@run_async 
def anal(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("anal")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def slap(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("slap")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def hentai(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("hentai")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def ero(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("ero")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def holo(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("holo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def blowjob(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("blowjob")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
 
@run_async 
def pussy(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("pussy")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def boobs(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("tits")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def pussypic(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("pussy_jpg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def waifu(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("waifu")
    r = request.get(nek)
    o = open(r, "rb")
    bot.send_sticker(chat_id = chat, sticker = o, reply_to_message_id = user)


@run_async 
def kiss(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("kiss")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def femdom(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("femdom")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def spank(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("spank")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def cuddle(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("cuddle")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def erok(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("erok")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def foxgirl(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("fox_girl")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def smug(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("smug")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def randomgif(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("random_hentai_gif")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def baka(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("baka")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)

@run_async 
def eronyuri(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("eroyuri")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
   
@run_async 
def eron(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("eron")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def cumpic(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("cum_jpg")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
      
@run_async 
def bj(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("bj")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def nekonsfw(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("nsfw_neko_gif")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
@run_async 
def solo(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("solo")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)

@run_async 
def tits(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("tits")
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = user)
           
@run_async 
def kuni(update: Update, context: CallbackContext ):
    if not NSFW = True:
      return
    bot = context.bot
    msg = update.effective_message
    user = update.effective_message.message_id
    chat = update.effective_chat.id
    nek = nekos.img("kuni")
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = user)
      
NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
KUNI_HANDLER = DisableAbleCommandHandler("kuni", kuni)
YURI_HANDLER = DisableAbleCommandHandler("yuri", yuri)
TRAP_HANDLER = DisableAbleCommandHandler("trap", trap)
FUTANARI_HANDLER = DisableAbleCommandHandler("futanari", futanari)
HOLOLEWD_HANDLER = DisableAbleCommandHandler("hololewd", hololewd)
LEWDKEMO_HANDLER = DisableAbleCommandHandler("lewdkemo", lewdkemo )
SOLOGIF_HANDLER = DisableAbleCommandHandler("sologif", sologif)
FEET_HANDLER = DisableAbleCommandHandler("feet", feet)
FEETGIF_HANDLER = DisableAbleCommandHandler("feetgif", feetgif)
CUMGIF_HANDLER = DisableAbleCommandHandler("cumgif", cumgif)
EROKEMO_HANDLER = DisableAbleCommandHandler("erokemo", erokemo)
LESBIAN_HANDLER = DisableAbleCommandHandler("lesbian", lesbian)
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
LEWDK_HANDLER = DisableAbleCommandHandler("lewdk", lewd)
NGIF_HANDLER = DisableAbleCommandHandler("ngif", ngif)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
KEMO_HANDLER = DisableAbleCommandHandler("kemonomimi", kemonomimi)
GASM_HANDLER = DisableAbleCommandHandler("gasm", gasm)
POKE_HANDLER = DisableAbleCommandHandler("poke", poke)
ANAL_HANDLER = DisableAbleCommandHandler("anal", anal) 
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
HENTAI_HANDLER = DisableAbleCommandHandler("hentai", hentai )
ERO_HANDLER = DisableAbleCommandHandler("ero", ero )
HOLO_HANDLER = DisableAbleCommandHandler("holo", holo )
BLOWJOB_HANDLER = DisableAbleCommandHandler("holo", holo )
PUSSY_HANDLER = DisableAbleCommandHandler("pussy", pussy )
BOOBS_HANDLER = DisableAbleCommandHandler("boobs", boobs )
PUSSYPIC_HANDLER = DisableAbleCommandHandler("pussypic", pussyic )
WAIFU_HANDLER = DisableAbleCommandHandler("waifu", waifu )
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss )
FEMDOM_HANDLER = DisableAbleCommandHandler("femdom", femdom )
SPANK_HANDLER = DisableAbleCommandHandler("spank", spank )
CUDDLE_HANDLER = DisableAbleCommandHandler("cuddle", cuddle )
EROK_HANDLER = DisableAbleCommandHandler("erok", erok )
FOXGIRL_HANDLER = DisableAbleCommandHandler("foxgirl", foxgirl )
SMUG_HANDLER = DisableAbleCommandHandler("smug", smug )
RANDOMGIF_HANDLER = DisableAbleCommandHandler("randomgif", randomgif )
BAKA_HANDLER = DisableAbleCommandHandler("baka", baka )
EROYURI_HANDLER = DisableAbleCommandHandler("eroyuri", eronyuri)
ERON_HANDLER = DisableAbleCommandHandler("eron", eron)
CUMPIC_HANDLER = DisableAbleCommandHandler("cumpic", cum)
BJ_HANDLER = DisableAbleCommandHandler("bj", bj)
NEKONSFW_HANDLER = DisableAbleCommandHandler("nekonsfw", nekonsfw)
SOLO_HANDLER = DisableAbleCommandHandler("solo", solo )
TITS_HANDLER = DisableAbleCommandHandler("tits", tits )
NSFW_HANDLER = DisableAbleCommandHandler("nsfw", nsfw )

dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(NSFW_HANDLER)
dispatcher.add_handler(YURI_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(FUTANARI_HANDLER)
dispatcher.add_handler(HOLOLEWD_HANDLER)
dispatcher.add_handler(LEWDKEMO_HANDLER)
dispatcher.add_handler(SOLOGIF_HANDLER)
dispatcher.add_handler(FEET_HANDLER)
dispatcher.add_handler(FEETGIF_HANDLER)
dispatcher.add_handler(CUMGIF_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(LEWDK_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(KEMO_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(ANAL_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(HENTAI_HANDLER)
dispatcher.add_handler(ERO_HANDLER)
dispatcher.add_handler(HOLO_HANDLER)
dispatcher.add_handler(BLOWJOB_HANDLER)
dispatcher.add_handler(PUSSY_HANDLER)
dispatcher.add_handler(BOOBS_HANDLER)
dispatcher.add_handler(PUSSYPIC_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(FEMDOM_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(SPANK_HANDLER)
dispatcher.add_handler(EROK_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(EROYURI_HANDLER)
dispatcher.add_handler(SOLO_HANDLER)
dispatcher.add_handler(BJ_HANDLER)
dispatcher.add_handler(ERON_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(CUMPIC_HANDLER)
dispatcher.add_handler(TITS_HANDLER)
dispatcher.add_handler(KUNI_HANDLER)

__help__ = """

Use /nsfw on/off or yes/no to manage nsfw control in your chat!! 
- /boobs: the balloons that boys like!! 
- /neko: neko neko ni!! cats like me!! 
- /feet: Peeps like to see feets too...
- /yuri: Now its a familiar thing.... girls kissing and teasing each other.... 
- /futanari: "im a girl who's a boy and likes to fuk girls" 
- /trap: "Im a boy from the inside" 
- /hololewd: Holo Lewds...?.. 
- /lewdkemo: Kemo Lewds.....?... 
- /sologif: Girls ruining themselves up....
- /cumgif: Milk flowing out like a waterfall..... 
- /erokemo: Ero-Kemo Images...?...
- /lesbian: The englis term for "yuri"... you know what i mean hehe.... 
- /wallpaper: Wallpapers....?....
- /lewdk: Kitsune Lewds....?..... 
- /ngif: Meow meow cat girls!! 
- /tickle: "Do i have a ticklish side?" 
- /lewd: Lewds!!! 
- /feed: Say Ahhhhhh!!!! 
- /eroyuri: Ero-Yuri source Images....?....
- /eron: Ero-Neko source Images...?....
- /cumpic: Milk but not in action...!! 
- /bj: Eating the hot rod!! action!! 
- /blowjob: Eating The hot rod!! Still pics?! 
- /nekonsfwgif: Catgirls but not safe!! 
- /solo: Girls ruining them but pics!! 
- /kemonomimi: KemonoMimi source Images....?....
- /gasm: Sends Orgasm pics!! 
- /poke: "My finger at ur body hitting hard!!!" 
- /anal: "But i poop from there!!"
- /hentai: obviously u know..... images
- /erofeet: feets but ero.... 
- /holo: Holo...?... 
- /tits: jiggly juggly tities!!! 
- /pussygif: My fav!! ah u know now..... 
- /holoero: Ero-Holo...?... there are too many combinations.... 
- /pussypic: Pics of pushies...... 
- /randomgif: Take out tht thingy...!! 
- /classic: Classical..?... 
- /kuni: Pussy Lick!! Yum!! 
- /waifu: Waifu?....!??... 
- /kiss: Lips..locked... dripping..juice..
- /femdom: Femdom?...!?... 
- /hug: "Am i your favorite!??!" 
- /erok: Combos.... Ero-kitsune?!.. 
- /foxgirl: Foxes are clever...so are girls... are you getting what i am saying?!..
- /ero: Ero!!.... 
- /smug: Smug...?...
- /baka: "Omae wa baka desu!!" 
 """
__mod_name__ = "LEWDS"
__command_list__ = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'sologif', 'feetgif', 'cumgif', 'erokemo', 'lesbian', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'eroyuri', 'eron', 'cumpic', 'bj', 'nekonsfw', 'solo', 'kemonomimi', 'gasm', 'poke', 'anal', 'hentai', 'erofeet', 'holo' 'blowjob', 'pussy', 'tits', 'holoero', 'pussypic', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'foxgirl', 'boobs', 'randomgif', 'ero', 'smug','baka']
 
