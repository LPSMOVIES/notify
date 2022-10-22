from config import DATABASE_NAME, DATABASE_URL, VOOT_API_URL, ZEE5_API_URL, BOT_USERNAME
from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.misc = self.db['misc']
        self.notify_urls = self.db['notify_urls']

    def getApiUrl(self, url):
        show_id = url.split("/")[-1]
        if "voot.com" in url:
            return VOOT_API_URL.format(show_id=show_id)
        elif "zee5.com" in url:
            return ZEE5_API_URL.format(show_id=show_id)

    async def get_bot_stats(self):
        return await self.misc.find_one({"bot": BOT_USERNAME})

    async def create_config(self):
        await self.misc.insert_one({
            'bot':BOT_USERNAME,
            'sleep_time': 0,
            'admins': [],
            'banned_users': [],
        })
    
    async def update_stats(self, dict):
        myquery = {"bot": BOT_USERNAME}
        newvalues = {"$set" : dict}
        return await self.misc.update_one(myquery, newvalues)
    
    async def add_notify_url(self, url, lang, domain):
        try:
            notify_url = await self.notify_urls.find_one({"url": url})
            if not notify_url:
                res = {
                    "url": url,
                    "lang": lang,
                    "site": domain,
                    "api_url":self.getApiUrl(url)
                }
                await self.notify_urls.insert_one(res)
                notify_url = await self.notify_urls.find_one({"url": url})
        except Exception as e:
            print(e)

        return notify_url

    async def delete_notify_url(self, url):
        myquery = {"url": url}
        return await self.notify_urls.delete_one(myquery)

    async def deleteall_notify_url(self):
        return await self.notify_urls.delete_many({})

    async def update_notify_url(self, url, value:dict, tag="$set"):
        myquery = {"url": url}
        newvalues = {tag : value}
        return await self.notify_urls.update_one(myquery, newvalues)

    async def filter_notify_url(self, dict):
        return self.notify_urls.find(dict)
        
db = Database(DATABASE_URL, DATABASE_NAME)
