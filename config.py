import os

from dotenv import load_dotenv
load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
BOT_USERNAME = os.environ.get("BOT_USERNAME")
BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", False)
VALIDITY = [int(i.strip()) for i in os.environ.get("VALIDITY").split(",")] if os.environ.get("VALIDITY") else [300,]
languages = os.environ.get("TRANSLATION_LANG").replace(r'\n', '\n').split("\n") #English, en \n Tamil, ta
IS_USER_ALLOWED_TO_CHANGE_LANGUAGE = is_enabled(os.environ.get("IS_USER_ALLOWED_TO_CHANGE_LANGUAGE", "False"), False)

#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

VOOT_API_URL = "https://psapi.voot.com/jio/voot/v1/voot-web/content/generic/series-wise-episode_curated?id=include%3A{show_id}&sort=episode%3Adesc&responseType=common"
ZEE5_API_URL = "https://gwapi.zee5.com/content/tvshow/{show_id}?translation=en&country=IN"
