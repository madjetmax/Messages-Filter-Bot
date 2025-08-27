from aiogram import Bot, Dispatcher
import asyncio

from config import *
import config
# packages
import handlers
import callbacks
import database as db
from database import engine as db_engine

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_routers( 
    handlers.router,
    callbacks.router,
)

async def main():
    # database
    await db_engine.create_db()

    # collect triggers in config
    config.KEYWORDS_TRIGGERS = [(kw.id, kw.word) for kw in await db.get_all_keywords()]    
    config.NAMES_TRIGGERS = [(name.id, name.name) for name in await db.get_all_trigger_names()]    
    config.PHRASES_TRIGGERS = [(phrase.id, phrase.text) for phrase in await db.get_all_phrases()]   

    # start bot polling
    print('bot launched')
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot stoped!")