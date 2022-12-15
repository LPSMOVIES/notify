import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "**Hi 👋\n\n  I am OTT Notification Bot. Doing the Amazing work of Providing links of Shows within seconds . Only Premium Users can Use me , So buy Subscription  From @LOGESH_BOTS** \n\n Powered by - @LOGESHBOTS")
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "**You Really Need Help ?🤔\n\n  Its a Zee5 / Voot / Hotstar Fastest Link provider Bot \nFirst You Need To Get access From @Logesh_bots Then You Can Use This Bot**")
    ABOUT_MESSAGE = os.environ.get("ABOUT_MESSAGE", "**Hey Bro I Am OTT NotificationBot \n\n i Can Give Notifications of New Episodes { ZEE5 VOOT HOTSTAR } \n\n My Father : [LOGESH](https://telegram.me/LOGESH_BOTS)\n Official Partner = [LOGESH BOTS](Https://telegram.me/LOGESHBOTS)**")

    ADD_ADMIN_TEXT = """Current Admins:
{}
Usage: /addadmin id
Ex: `/addadmin 14035272, 14035272`
To remove a admin,
Ex: `/addadmin remove 14035272`
To remove all admins,
Ex: `/addadmin remove_all`
"""

    BANNED_USERS_LIST = """Current Banned Users:
{}
Usage: /ban id
Ex: `/ban 14035272, 14035272`
To remove a banned user,
Ex: `/ban remove 14035272`
To remove all banned user,
Ex: `/ban remove_all`
"""

    NOTIFY_URLS_LIST = """Current Urls Users:
{}
Usage: /add_url id
Ex: `/add_url Kannada https://www.zee5.com/tv-shows/details/vaidehi-parinaya/0-6-4z5173773`
To remove a url,
Ex: `/add_url remove https://www.zee5.com/tv-shows/details/vaidehi-parinaya/0-6-4z5173773`
To remove all urls,
Ex: `/add_url remove_all`
"""

    SUBSCRIPTION_REMINDER_MESSAGE = """**Your subscription is gonna end soon. 
    
Renew your subscription to continue this service contact @Logesh_bots:

Details:
User ID: {user_id}

Subscription Date: {subscription_date}

Expiry Date: {expiry_date}

Subscription Peroid Remaining: {time_remaining}

Allowed Languages: {allowed_languages}

Banned: {banned_status}
**"""

    HELP_REPLY_MARKUP = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Help', callback_data=f'help_command'),
            InlineKeyboardButton('Language', callback_data=f'lang_command'),

        ],

        [
            InlineKeyboardButton('About', callback_data=f'about_command'),
            InlineKeyboardButton('My Plan', callback_data=f'info_command'),    
        ],
        [
            InlineKeyboardButton('Close', callback_data=f'delete'),    
        ],

    ])

    HOME_BUTTON_MARKUP = InlineKeyboardMarkup([[InlineKeyboardButton('Home', callback_data='start_command')]])

