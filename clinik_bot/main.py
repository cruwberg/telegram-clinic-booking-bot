import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, booking  # подключаем оба файла

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # подключаем роутеры
    dp.include_router(start.router)
    dp.include_router(booking.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

