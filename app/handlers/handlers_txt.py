from aiogram import F, Router
from aiogram.types import Message


router_txt = Router()


@router_txt.message(F.text == "Как дела?")
async def heo_are_you(message: Message):
    await message.reply("Хорошо")


@router_txt.message(F.text == "Привет")
async def hello_message(message: Message):
    await message.reply("Приветствую!")



@router_txt.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"ID фотографии: {message.photo[-1 ].file_id}")