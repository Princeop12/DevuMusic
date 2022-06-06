# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by Mr Prince

import requests
from pyrogram import idle
from pyrogram import Client as Bot
from callsmusic.callsmusic import client as USER

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

async def main():
    async with bot:
        try:
            await USER.join_chat(L00NeY_TunesxD)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            print(e)
            pass

bot.start()
run()
idle()
