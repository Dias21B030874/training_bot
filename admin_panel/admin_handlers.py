from aiogram import Router, types, F
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import UserResponse
from datetime import datetime, date
from sqlalchemy import func


ADMIN_IDS = [779889025, 669233477]

router = Router()

@router.message(F.text == "/admin")
async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Доступ запрещён.")
        return
    await message.answer(
        "Панель администратора:\n"
        "/users — список пользователей\n"
        "/broadcast — рассылка\n"
        "/add_knowledge — добавить в базу знаний"
    )

@router.message(F.text == "/users")
async def list_users(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    with SessionLocal() as session:
        users = session.query(UserResponse).all()
        if not users:
            await message.answer("Нет пользователей.")
            return
        text = "\n\n".join(
            [
                f"ID: {u.user_id}\n"
                f"Имя: {u.name}\n"
                f"Телефон: {u.phone}\n"
                f"Источник: {u.source}\n"
                f"Желание: {u.desired_activity}\n"
                f"Рекомендация Gemini: {u.gemini_recommendation}\n"
                f"Лучшее направление: {u.best_direction}"
                for u in users
            ]
        )
        await message.answer(text[:4096])

@router.message(F.text.startswith("/broadcast"))
async def broadcast(message: types.Message, bot):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text.replace("/broadcast", "").strip()
    if not text:
        await message.answer("Введите текст рассылки после команды.")
        return
    with SessionLocal() as session:
        users = session.query(UserResponse.user_id).distinct()
        for user in users:
            try:
                await bot.send_message(user.user_id, text)
            except Exception:
                continue
    await message.answer("Рассылка завершена.")


@router.message(F.text.startswith("/add_knowledge"))
async def add_knowledge(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    text = message.text.replace("/add_knowledge", "").strip()
    if not text:
        await message.answer("Введите текст блока после команды.")
        return
    with open("knowledge_base.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n---\n")
    await message.answer("Блок добавлен в базу знаний.")


@router.message(F.text == "/dashboard")
async def dashboard(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Доступ запрещён.")
        return
    with SessionLocal() as session:
        # Кол-во новых записей за сегодня
        today = date.today()
        new_today = session.query(UserResponse).filter(
            func.date(UserResponse.id) == today
        ).count()

        # Кол-во записей по направлениям
        directions = session.query(
            UserResponse.desired_activity, func.count(UserResponse.id)
        ).group_by(UserResponse.desired_activity).all()
        directions_text = "\n".join(
            f"{d[0]}: {d[1]}" for d in directions
        )

        # Кол-во людей, дошедших до кнопки оплаты (payment)
        # Предполагаем, что если есть запись в таблице Payment — дошёл до оплаты
        from database.models import Payment
        paid_count = session.query(Payment.user_id).distinct().count()

    await message.answer(
        f"📊 <b>Дашборд</b>\n"
        f"Новых записей сегодня: {new_today}\n"
        f"Записи по направлениям:\n{directions_text}\n"
        f"Дошли до оплаты: {paid_count}"
    )