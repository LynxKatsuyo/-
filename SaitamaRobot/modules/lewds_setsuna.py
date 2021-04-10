import nekos
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

neko = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'erokemo', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'eroyuri', 'eron', 'bj', 'solo', 'kemonomimi', 'gasm', 'poke', 'anal', 'hentai', 'erofeet', 'holo' 'blowjob', 'pussy', 'tits', 'holoero','pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'boobs', 'smallboobs', 'hug', 'ero', 'smug','baka', 'woof']

@run_async
def lewd_setsuna(update: Update, context: CallbackContext ):
  bot = context.bot 
  msg = str(update.effective_message) 
  msg_id = update.effective_message.message_id 
  chat = update.effective_chat.id
  msgs = msg.replace("/"," ")
  for i in neko:
    if msgs in neko:
      img = i
    else:
      pass 
  if msgs == 'sologif':
    img = 'solo' 
  elif msgs == 'feetgif':
    img = 'feetg' 
  elif msgs == 'cumgif':
    img = 'cumg' 
  elif msgs == 'lesbian':
    img = 'les' 
  elif msgs == 'cumpic':
    img = 'cum_jpg' 
  elif msgs == 'nekonsfwgif':
    img = 'nsfw_neko_gif'
  elif msgs == 'pussypic':
    img ='pussy_jpg'
  elif msgs == 'foxgirl':
    img = 'fox_girl'
  elif msgs == 'randomgif':
    img = 'random_hentai_gif'
  else:
    return
  nek = nekos.img(img)
  if nek.endswith('gif'):
    bot.send_animation(chat_id = chat, animation = nek, reply_to_message_id = msg_id )
  else:
    bot.send_photo(chat_id = chat, photo = nek, reply_to_message_id = msg_id)
    
nekkoo = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'erokemo', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'eroyuri', 'eron', 'bj', 'solo', 'kemonomimi', 'gasm', 'poke', 'anal', 'hentai', 'erofeet', 'holo' 'blowjob', 'pussy', 'tits', 'holoero','pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'boobs', 'smallboobs', 'hug', 'ero', 'smug','baka', 'woof', 'sologif', 'feetgif', 'cumgif', 'lesbian', 'cumpic', 'nekonsfwgif', 'pussypic', 'foxgirl', 'randomgif' ]


NEKOS_HANDLER = DisableAbleCommandHandler(nekkoo, lewd_setsuna)
dispatcher.add_handler(NEKOS_HANDLER)

__help__ = """

*Here is the help for the Lewd module:*

- /boobs: the balloons that boys like!! 
- /smallboobs: Some love them!! not huge... 
 - /neko: neko neko ni!! cats like me!! 
 - /feet: Peeps like to see feets too...
 - /yuri: Now its a familiar thing.... girls kissing and teasing each other.... 
 - /trap: "Im a boy from the inside" 
 - /futanari: "im a girl who's a boy and likes to fuk girls" 
 - /hololewd: Holo Lewds...?.. 
 - /lewdkemo: Kemo Lewds.....?... 
 - /sologif: Girls ruining themselves up..... 
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
 - /kiss: Lips..locked... dripping..juice... 
 - /femdom: Femdom?...!?... 
 - /hug: "Am i your favorite!??!" 
 - /erok: Combos.... Ero-kitsune?!.. 
 - /foxgirl: Foxes are clever...so are girls... are you getting what i am saying?!... 
 - /titsgif: Jiggle Juggle Titites!! 
 - /ero: Ero!!.... 
 - /smug: Smug...?...
 - /baka: "Omae wa baka desu!!" 
 """
__mod__ = "LEWDS"
__command_list__ = nekkoo
__handlers__ = [NEKOS_HANDLER]
