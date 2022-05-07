from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Графік')
b2 = KeyboardButton('/Розташування')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/Відправити контакт', request_contact=True)
# b5 = KeyboardButton('/Відправити локацію', request_location=True)


client_kb = ReplyKeyboardMarkup(resize_keyboard=True)

client_kb.row(b1, b2, b3)#.add(b4).insert(b5)