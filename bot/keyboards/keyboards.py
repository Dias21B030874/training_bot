from aiogram import types


def main_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📚 О студии")],
            [types.KeyboardButton(text="💳 Оплатить")],
            [types.KeyboardButton(text="Записаться на тренировку")],
            [types.KeyboardButton(text="1С кабинет")],  
        ],
        resize_keyboard=True
    )

def source_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Instagram")],
            [types.KeyboardButton(text="Друзья")],
            [types.KeyboardButton(text="Сайт")],
            [types.KeyboardButton(text="Проходил мимо")],
            [types.KeyboardButton(text="Другое")]
        ],
        resize_keyboard=True
    )

def training_options_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Pilates")],
            [types.KeyboardButton(text="Reformer")],
            [types.KeyboardButton(text="Фитнес")],
            [types.KeyboardButton(text="Силовая")],
            [types.KeyboardButton(text="Растяжка")],
            [types.KeyboardButton(text="Пока не знаю")]
        ],
        resize_keyboard=True
    )