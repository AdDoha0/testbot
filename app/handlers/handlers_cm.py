
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from aiogram import Router

router_cm = Router()


@router_cm.message(Command("help"))
async def help_cm(message: Message):
    await message.answer("чем могу помочь? /help")


@router_cm.message(CommandStart())
async def start_comand(message: Message):
    await message.reply(f"Привет! Это тестовое бот для отправки /start, ваш id: {message.from_user.id}" )



