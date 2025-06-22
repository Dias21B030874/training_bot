from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define the admin panel keyboard
admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# Add buttons to the keyboard
admin_keyboard.add(KeyboardButton("Просмотр базы"))
admin_keyboard.add(KeyboardButton("Отправка рассылки"))
admin_keyboard.add(KeyboardButton("Добавить блок в базу знаний"))
admin_keyboard.add(KeyboardButton("Выход"))