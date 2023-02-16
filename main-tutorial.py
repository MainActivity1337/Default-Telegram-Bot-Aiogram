import aiogram # тут мы импортируем библиотеку aiogram
from aiogram import Bot, dispatcher, executor, types # это мы из aiogram импортируем все важные материалы  для создания нашего тг бота


TOKEN_BOT = "" # тут в двойных кавычках вы пишете токен вашего бота (получить токен бота - @BotFather)

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)

# начало  кода команды /start
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
	await bot.send_meesage(message.from_user.id, f"Ответ на комнду /start")
# конец кода команды /start
# можно копировать эту команду и менять под себя её!


# эта часть кода отвечает за запуск нашего бота!
if __name__ == '__main__':
	executor.start_polling(dp)