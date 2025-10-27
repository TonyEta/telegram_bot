import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())




bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Юлєчка-булочка")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)  #видаляє надіслані в бот повідомлення за час коли бот не був запущений
    await dp.start_polling(bot)


asyncio.run(main())