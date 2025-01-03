from bot_token import api_token as TOKEN_API

import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers import router




async def main():
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is off')
