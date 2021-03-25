#made by @DontKnowWhoRU using @TheChizuruBot 

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from telethon.errors.rpcerrorlist import YouBlockedUserError


@run_async
async def neko(hex):
    chat = "@TheChizuruBot"
    async with hex.client.conversation(chat) as conv:
        start_msg = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message("/neko" )
        await hex.edit("cumming.... ")
        result = await conv.get_response()
        await hex.client.send_read_acknowledge(conv.chat_id)
    await hex.respond(result) 
    
__help__ = """ 
Its still uncomplete just trying... 

For now i have only one command-
°`/neko`*:* Fetches neko images

"""
    
NEKO_HANDLER = MessageHandler(Filters.all & Filters.group, neko )

dispatcher.add_handler(NEKO_HANDLER)
__mod_name__ = "Lewd" 
__command_list__ = ["neko"]
__handlers__ = [NEKO_HANDLER]



