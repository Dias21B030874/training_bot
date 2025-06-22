from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.keyboards.keyboards import source_keyboard, training_options_keyboard, main_keyboard
from bot.states.forms import Form, OneCForm
from services.gemini import GeminiRecommender
from database.db import SessionLocal
from database.models import UserResponse

gemini = GeminiRecommender()
router = Router()

@router.message(F.text == "/start")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Как вас зовут?")
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer("Пожалуйста, укажите ваш телефон (например, +7 ХХХ ХХХ ХХ ХХ):")

@router.message(Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Form.source)
    await message.answer("Откуда вы о нас узнали?", reply_markup=source_keyboard())

@router.message(Form.source)
async def process_source(message: types.Message, state: FSMContext):
    await state.update_data(source=message.text)
    await state.set_state(Form.problem)
    await message.answer("Что вас беспокоит? (Опишите кратко)", reply_markup=types.ReplyKeyboardRemove())

@router.message(Form.problem)
async def process_problem(message: types.Message, state: FSMContext):
    await state.update_data(problem=message.text)
    data = await state.get_data()
    # Получаем рекомендацию от Gemini
    recommendation, best_direction = gemini.get_recommendation_with_best(
        user_problem=message.text,
        user_name=data.get("name"),
        user_phone=data.get("phone")
    )
    await state.update_data(gemini_recommendation=recommendation)
    await state.update_data(best_direction=best_direction)
    await state.set_state(Form.direction)
    await message.answer(
        f"{recommendation}\n\nВыберите направление из списка ниже. "
        f"Мы рекомендуем: <b>{best_direction}</b>",
        reply_markup=training_options_keyboard()
    )

@router.message(Form.direction)
async def process_direction(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # Сохраняем в БД!
    with SessionLocal() as session:
        user = UserResponse(
            user_id=message.from_user.id,
            name=data.get("name"),
            phone=data.get("phone"),
            source=data.get("source"),
            concern=data.get("problem"),
            desired_activity=message.text,
            gemini_recommendation=data.get("gemini_recommendation"),
            best_direction=data.get("best_direction")
        )
        session.add(user)
        session.commit()
    await state.set_state(Form.payment)
    await message.answer(
        f"Спасибо! Ваши ответы сохранены.\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Источник: {data['source']}\n"
        f"Проблема: {data['problem']}\n"
        f"Выбранное направление: {message.text}\n\n"
        "Супер! Можешь записаться на пробное занятие. Стоимость — 1000₽",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text="💳 Оплатить")]],
            resize_keyboard=True
        )
    )

@router.message(F.text == "💳 Оплатить")
async def process_payment(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Ты успешно записан! Скоро свяжемся с тобой для подтверждения времени.",
        reply_markup=main_keyboard()
    )

# Кнопка "О студии"
@router.message(F.text == "📚 О студии")
async def about_studio(message: types.Message):
    await message.answer(
        "📚 <b>О студии</b>\n"
        "\n"
        "<b>Pilates</b> — система упражнений для укрепления мышц и улучшения осанки.\n"
        "<b>Reformer</b> — тренировки на специальном тренажёре для глубоких мышц.\n"
        "<b>Преимущества:</b> индивидуальный подход, современное оборудование, опытные тренеры.\n"
        "\n"
        "<b>Расписание:</b> ежедневно 8:00–22:00\n"
        "<b>Адрес:</b> ул. Примерная, 1\n"
        "<b>Контакты:</b> +7 777 123 45 67\n"
        "<b>Сайт:</b> https://yourstudio.example.com"
    )

@router.message(F.text == "1С кабинет")
async def one_c_link(message: types.Message, state: FSMContext):
    await message.answer(
        "Ссылка на кабинет 1С: https://1c.example.com\n"
        "Введите пароль для входа:"
    )
    await state.set_state(OneCForm.password)

@router.message(OneCForm.password)
async def one_c_password(message: types.Message, state: FSMContext):
    # Просто заглушка, пароль никуда не отправляется
    await message.answer("Спасибо! (Заглушка: интеграция с 1С будет позже)")
    await state.clear()


@router.message(F.text.in_({"/help", "/start", "/"}))
async def help_command(message: types.Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — начать анкету\n"
        "/help — список команд\n"
        "/admin — панель администратора (для админов)\n"
        "/dashboard — дашборд (для админов)\n"
        "Или используйте кнопки меню 👇"
    )