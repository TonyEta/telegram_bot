from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привіт, я віртуальний помічник")

@user_private_router.message(Command('menu'))
async def echo(message: types.Message):
    await message.answer("Меню:")

@user_private_router.message(Command('about'))
async def echo(message: types.Message):
    await message.answer("Опис бота")

@user_private_router.message(Command('payment'))
async def echo(message: types.Message):
    await message.answer("Варіанти оплати")

@user_private_router.message(Command('shipping'))
async def echo(message: types.Message):
    await message.answer("Варіанти доставки")