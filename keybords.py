from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_val = KeyboardButton('Хочу валентинку❤️')
button_about = KeyboardButton('Обратная связь')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(button_val, button_about)
