import asyncio

from aiogram import Bot, Dispatcher
from logging import basicConfig, INFO

from confing import TOKEN
from app.handlers.__init__ import setup_routes
from app.data import database as db




bot = Bot(token=TOKEN)
dp = Dispatcher()


async def on_startup(_):
    await db.



async def main():
    setup_routes(dp)
    await dp.start_polling(bot)



if __name__ == '__main__':
    basicConfig(level=INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
