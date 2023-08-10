from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from decouple import config
from database.sql_commands import Database
from aiogram.types import ParseMode

from aiogram import executor

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

db = Database()

@dp.message_handler(Command('start'))
async def start(message: types.Message):
    user_id = message.from_user.id
    db.insert_user(user_id)
    await message.reply("Вы были успешно зарегистрированы!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)