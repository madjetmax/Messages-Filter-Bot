from aiogram import Bot, Dispatcher
import asyncio

from config import *
import config
# packages
import handlers
import callbacks
import database as db
from database import engine as db_engine
from utils.parse_text import normalize

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_routers( 
    handlers.router,
    callbacks.router,
)

async def collect_triggers():
    config.KEYWORDS_TRIGGERS = [(kw.id, kw.word) for kw in await db.get_all_keywords()]    
    config.NAMES_TRIGGERS = [(name.id, name.name) for name in await db.get_all_trigger_names()]    
    config.PHRASES_TRIGGERS = [
        (
            phrase.id, phrase.text, 
            # collect phrase into full string
            "".join(normalize(word) for word in phrase.text.split(" "))
        ) 
        for phrase in await db.get_all_phrases()
    ]   
    print(config.PHRASES_TRIGGERS)


async def main():
    # database
    await db_engine.create_db()

    await collect_triggers()
    
    # start bot polling
    print('bot launched')
    # skip updates on start
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stoped!")