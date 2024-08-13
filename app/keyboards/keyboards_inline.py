from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


command_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Заучивание имен", callback_data="names_learn")],
    [InlineKeyboardButton(text="Повторение имен", callback_data="names_repeat")],
    [InlineKeyboardButton(text="Все Имена", callback_data="all_names")],
    [InlineKeyboardButton(text="Поддержка автора", callback_data="support_author")],
])
