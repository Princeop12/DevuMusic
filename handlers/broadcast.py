# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS

DARK_IMG = "https://telegra.ph/file/72e0caff8514e372b55a1.jpg"

@Client.on_message(filters.command("gcast"))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        hyper = await message.reply("`sᴛᴀʀᴛᴇᴅ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴡᴀɪᴛ👩‍💻`")
        if not message.reply_to_message:
            await hyper.edit("**__ɢɪᴍᴍɪ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴄᴀsᴛ🤷‍♀️...__**")
            return
        devu = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, Broken)
                sent = sent+1
                await hyper.edit(f"`ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ` \n\n**sᴜᴄᴄᴇssғᴜʟʟ ɪɴ:** `{sent}` ᴄʜᴀᴛs👾 \n**ᴜɴsᴜᴄᴄᴇssғᴜʟʟ ɪɴ:** {failed} ᴄʜᴀᴛs🗑️")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_photo(DARK_IMG, caption=f"`sᴜᴄᴄᴇsғᴜʟʟʏ ᴅᴏɴᴇ🧚‍♀️` \n\nsᴜᴄᴄᴇssғᴜʟʟ**:** `{sent}` ᴄʜᴀᴛs \n**ғᴀɪʟᴇᴅ :** {failed} ᴄʜᴀᴛs")
