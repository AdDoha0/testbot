
# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Именна Аллаха"), KeyboardButton(text="Повторение")],
#     [KeyboardButton(text="Заучивание имен")]
# ],
#                             resize_keyboard=True,
#                             input_field_placeholder="Выберите пункт меню")



from aiogram.types import KeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder

names = [str(i) + "Ar-Rahman" for i in range(1, 101)]


async def reply_name():
    keyboard = ReplyKeyboardBuilder()
    for name in names:
        keyboard.add(KeyboardButton(text=name))
    return keyboard.adjust(4).as_markup()