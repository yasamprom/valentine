import os

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

import db
import keybords as kb

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: types.Message, state: FSMContext):
    target = message.from_user.username
    await message.answer("Напиши текст валентинки, она будет анонимно отправлена" + target +
                         "Чтобы начать получать валентинки нажми \"Хочу валентинку\"",
                         reply_markup=kb.main_kb)
    await db.add_user_to_db(str(message.from_user.id) + ": " + message.from_user.username)
    await state.set_state('waiting text')
    await state.update_data(target_id=message.get_args())


@dp.message_handler(state='*', text=['Обратная связь'])
async def process_donate(message: types.Message):
    await message.answer("По вопросам и отзывам можно писать сюда @bryansk_sever111",
                         reply_markup=kb.main_kb)


@dp.message_handler(text=['Хочу валентинку❤️'], state='*')
async def process_start_command(message: types.Message):
    link = 't.me/sweetfunnyvalentine_bot?start=' + str(message.from_user.id)
    await message.answer("Вот твоя ссылка\n" + link + '\n' +
                         "Запости куда хочешь. Тот, кто перейдет по ссылке, сможет "
                         "отправить анонимную валентинку тебе ❤️", reply_markup=kb.main_kb)


@dp.message_handler(state='waiting text')
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        target_id = data['target_id']
        await bot.send_message(target_id, "Тебе что-то написали:\n" + message.text)
    await message.answer("Ура, отправили валентинку!")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


