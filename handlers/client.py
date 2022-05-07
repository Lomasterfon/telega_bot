from aiogram import types, Dispatcher
from create_bot import bot
from keyboard import client_kb
from data_base import sqlite_db
# from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привіт', reply_markup=client_kb)
        await message.delete()
    except:
        await message.reply('Напишіть боту в ОП:\nhttps://t.me/ConverterCurrency_Bot')


# @dp.message_handler(commands=["Графік"])
async def time_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт 9:00 - 19:00, Сб-Нд 10:00 - 18:00, Обід 12:30 - 13:00')


# @dp.message_handler(commands=["Розташування"])
async def map_location(message: types.Message):
    await bot.send_message(message.from_user.id, 'вул. Прорізна, 3, офiс №33')


# @dp.message_handler(commands=["Меню"])
async def menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(time_schedule, commands=["Графік"])
    dp.register_message_handler(map_location, commands=["Розташування"])
    dp.register_message_handler(menu_command, commands=["Меню"])
