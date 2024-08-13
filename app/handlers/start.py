
from aiogram.types import Message
from aiogram.filters import CommandStart

from aiogram import Router

import app.keyboards.keyboards_inline as kb_inline


router_start = Router()



@router_start.message(CommandStart())
async def start_comand(message: Message):
    await message.answer(f"Ассаламу алейкум! Я помогу вам выучить имена Аллаха.\nВыберите пункт меню",
                         reply_markup=kb_inline.command_start)



