# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """Hey {}\n\nMyself {} \nA simple , lagfree and flexible music robot!\nIf you facing any issue related to this music bot then please join @{}\nFor more help you can explorer help menu by tapping on /help !"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="Updates", url=f"https://t.me/L00NeY_TunesxD0"),
                    InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Owner✨", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Source", callback_data="repo_k"),
                ],                
                [                    
                    InlineKeyboardButton(text="Help & Commands!", callback_data="help_"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """Hoi {}\nHere is the help menu choose your desireoption nd explorer it!!\nFor any kind of help or query Just join @{} and ask your query!!"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="Basic!", callback_data="basic_"),
            InlineKeyboardButton(text="Advance!", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="Close", callback_data="close_"),
            InlineKeyboardButton(text="Back", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Hoi, Here is the help menu choose your desireoption nd explorer it!!\nFor any kind of help or query Just join @{SUPPORT_GROUP} and ask your query!!"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="Basic!", callback_data="basic_"),
                InlineKeyboardButton(text="Advance!", callback_data="admin_cmd"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close_"),
                InlineKeyboardButton(text="Back", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "repo_k":
        REPO_MSG = f"""Hey, Here is the source code of {BOT_NAME} \nSo deploy your own and enjoy and don't forget to fork nd to give star 😕!!"""
        REPO_BUTTONS = [
            [
                InlineKeyboardButton(text="Source", url="tere papa ka nahi jo mila hai usse hi use kar chutiye repo lega"),
                InlineKeyboardButton(text="Back", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            REPO_MSG,
            reply_markup=InlineKeyboardMarkup(REPO_BUTTONS)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Hey, Myself {BOT_NAME} \nA simple , lagfree and flexible music robot!\nIf you facing any issue related to this music bot then please join @{SUPPORT_GROUP}\nFor more help you can explorer help menu by tapping on /help !"""
        START_BUTTON = [
                    [
                        InlineKeyboardButton(text="Updates", url="https://t.me/L00NeY_TunesxD"),
                        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                    ],
                    [
                        InlineKeyboardButton(text="Owner✨", url=f"https://t.me/{OWNER_USERNAME}"),
                        InlineKeyboardButton(text="Source", callback_data="repo_k"),
                    ],                
                    [                    
                        InlineKeyboardButton(text="Help & Commands!", callback_data="help_"),
                    ],      
        ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "basic_":
        B_HELP = """
`Basics Commands !!`

/play (query, ytlink, audio file) - use this command and enjoy music
/ytp (query) - Use it for better search music!!
/song (query) - Download your favourite songs using this command!
/search (query) - This command will give you youtube search of your query!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close_"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin_cmd":
        A_HELP = """
`Admins Commands!!`

/pause - To pause the song!
/resume - Resume paused song!
/skip - skip to the next song!
/end - End the stream!
/joinub - To invite assistant in your group!


`Sudo Command!`

/rmf - To clean Download file from database!
/rmw - To clean raw files from database!
/dclean - To clean files from server!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close_"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        calllback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
