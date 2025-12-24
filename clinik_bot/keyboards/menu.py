from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🩺 Записаться на приём")],
        [KeyboardButton(text="📍 Контакты"), KeyboardButton(text="ℹ️ О клинике")]
    ],
    resize_keyboard=True
)
