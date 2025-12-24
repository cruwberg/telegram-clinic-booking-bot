from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def specialists_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Терапевт", callback_data="spec_Терапевт")],
        [InlineKeyboardButton(text="Стоматолог", callback_data="spec_Стоматолог")],
        [InlineKeyboardButton(text="Кардиолог", callback_data="spec_Кардиолог")]
    ])

def date_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сегодня", callback_data="date_Сегодня")],
        [InlineKeyboardButton(text="Завтра", callback_data="date_Завтра")]
    ])

def time_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="10:00", callback_data="time_10:00")],
        [InlineKeyboardButton(text="11:00", callback_data="time_11:00")],
        [InlineKeyboardButton(text="12:00", callback_data="time_12:00")]
    ])
