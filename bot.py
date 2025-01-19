import asyncio 
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from dotenv import dotenv_values
from backend import get_random_otvet_line, generate_random_ip

config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    await message.answer('ку-ку')

@dp.message(F.text == "рома")
async def small_talk_message(message):
    await message.reply('Знай: Тимур лох')

@dp.message(F.text == "Как дела?")
async def small_talk_message(message):
    await message.reply(f'Это вить твой {get_random_otvet_line()}')

@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_otvet_line())

async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())