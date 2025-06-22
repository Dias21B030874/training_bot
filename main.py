import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from bot.bot_instance import dp, bot
import os
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.strategy import FSMStrategy
from bot.bot_instance import dp 
from bot.handlers import start, payment_handlers, info_handlers, error_handlers
from database.db import engine
from database.base import Base
from admin_panel import admin_handlers
from aiogram.types import BotCommand

def create_db():
    Base.metadata.create_all(bind=engine)

async def main():
    load_dotenv()
    create_db()

    await bot.set_my_commands([
    BotCommand(command="start", description="Начать анкету"),
    BotCommand(command="help", description="Справка"),
    BotCommand(command="admin", description="Панель администратора"),
    BotCommand(command="dashboard", description="Дашборд"),
    ])
    dp.include_router(start.router)
    dp.include_router(admin_handlers.router)
    
    # dp.include_router(payment_handlers.router)
    # dp.include_router(info_handlers.router)
    # dp.include_router(error_handlers.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())