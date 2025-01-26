import asyncio 
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from dotenv import dotenv_values
from backend import get_random_otvet_line, generate_random_ip
from Users import create_user, read_user

config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    user_id = message.from_user.id
    config = {
        'ip': generate_random_ip(),
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
        'language_code': message.from_user.language_code
    }

    create_user(user_id = user_id, config=config)
    first_name = config['first_name']
    await message.reply(f'Привет, {first_name}!\nЯ уже знаю как тебя зовут.')

@dp.message(F.text == "Где?")
async def small_talk_message(message):
    await message.reply('Нигде, бабки гони чушпан')

@dp.message(F.text == "Как дела?")
async def small_talk_message(message):
    user_id = message.from_user.id
    ip = read_user(user_id=user_id)['ip']
    await message.reply(f'Я знаю, где ты живёшь: {ip}')

    if lang == 'en':
        await message.reply(f'Говори на Русском')

@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_otvet_line())

async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())