import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router



ALLOWED_UPDATES = ['message', 'edited_message']  # фільтр оновлень які прийдуть нашому боту, обмеження типів Update

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)




async def main():
    print('бот запущено')
    await bot.delete_webhook(drop_pending_updates=True)  # видаляє надіслані в бот повідомлення за час коли бот не був запущений
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())