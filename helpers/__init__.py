import translators as ts
from config import VALIDITY

from database import db, get_user
from pyrogram.types import InlineKeyboardButton
from .human_time import human_time


class temp(object):
    ADMINS_LIST = None
    SLEEP_TIME = None
    BANNED_USERS = []
    NOTIFY_URLS = [] # only links
    ZEE5:list = {}
    COLORS:dict = {}
    LANG = {}

async def translate(text, from_language='en', to_language=None):  
    return ts.google(text, from_language=from_language, to_language=to_language) if to_language != from_language else text

def user_allowed_langauage(user, lang):
    return f"Allow {lang} ✅" if lang not in user['allowed_languages'] else f"Disallow {lang} ❌"

async def get_user_info_button(user_id):
    user = await get_user(user_id)
    btn = [[InlineKeyboardButton(text=f"Add {human_time(time_in_s)}", callback_data=f'validity#{user_id}#{time_in_s}')] for time_in_s in VALIDITY]
    avl_serial_lang = []
    async for lan in await db.filter_notify_url({}):
        language = lan['lang']
        avl_serial_lang.append(language) if language not in avl_serial_lang else []
    btn.append([InlineKeyboardButton(text=f"{user_allowed_langauage(user, serial_lang)}", callback_data=f'allowlang#{user_id}#{serial_lang}') for serial_lang in avl_serial_lang
    ])
    btn.append([InlineKeyboardButton("Remove from database", callback_data=f"deleteuser#{user_id}")])
    btn.append([InlineKeyboardButton("Remove access", callback_data=f"removeaccess#{user_id}")])
    btn.append([InlineKeyboardButton("Close", callback_data="delete")])
    return btn

def listToString(s):
    # return string
    return " ".join(s)