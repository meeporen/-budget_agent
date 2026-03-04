import asyncio
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from config import settings
from bot.handlers import router


dp = Dispatcher()
dp.include_router(router)
bot = Bot(token=settings.telegram_bot_token)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())