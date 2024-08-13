from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command



import app.keyboards.keyboards_reply as kb_reply

router_name = Router()

@router_name.message(Command("names"))
async def handlers_name(message: Message):
    await message.answer("Все имена:", reply_markup=await kb_reply.reply_name())