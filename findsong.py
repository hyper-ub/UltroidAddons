# Ultroid Userbot
# Made by senku

"""
✘ Commands Available

• `{i}findsong <reply to song>`
   Identify the song name
"""

import requests
from telethon import events
from . import *
from telethon.errors.rpcerrorlist import YouBlockedUserError


@ultroid_cmd(pattern="findsong$")
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, "Reply to an audio message.")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    snku = await eor(event, "Identifying the song")
    async with ultroid_bot.conversation(chat) as conv:
        try:
            start_msg = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await snku.edit("An error while identifying the song. Try to use a 5-10s long audio message.")
            await snku.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await snku.edit("Please unblock (@auddbot) and try again")
            return
    namem = f"**Song Name : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await snku.edit(namem)
    

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
