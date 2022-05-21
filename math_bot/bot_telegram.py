from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import calculate


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
	await message.answer(calculate.calculation(message.text))

executor.start_polling(dp, skip_updates=True)