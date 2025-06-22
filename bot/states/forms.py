from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    phone = State()
    source = State()
    problem = State()
    direction = State()
    payment = State()

class OneCForm(StatesGroup):
    password = State()