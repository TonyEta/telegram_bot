from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command


user_private_router = Router()



@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привіт, я віртуальний помічник")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Меню:")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("Опис бота")

@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("Варіанти оплати")

@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer("Варіанти доставки")


@user_private_router.message(F.text)
async def test_cmd(message: types.Message):
    await message.answer("Це магічний фільтр")
