from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_val = KeyboardButton('Хочу валентинку❤️')
button_about = KeyboardButton('Поддержать проект💳')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_val, button_about)
