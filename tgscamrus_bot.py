import asyncio
import logging
#import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
#from bs4 import BeautifulSoup

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6893212655:AAGE741DMRwiAa9KNy-WpZXMXdhczJCzlUA")
# Диспетчер
dp = Dispatcher()

#url = 'https://igropad.com/ru/games-list'

#if response.status_code == 200:
#    soup = BeautifulSoup(response.text, 'html.parser')



# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.answer("Вас приветствует GameDevStart бот! Этот бот поможет вам выбрать игру если вы заскучали. Напишите комаду '/continue' чтобы начать работу")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())