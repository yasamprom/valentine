from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.deep_linking import decode_payload
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
import keybords as kb
import os

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


NOTIFICATION = 1


async def save_id(user_id):
    f = open('users.txt', 'a')
    f.write(str(user_id) + '\n')
    f.close()


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: types.Message, state: FSMContext):
    await message.answer("Напиши тут валентинку человеку, который опубликовал ссылку. "
                         "Я отправлю ее анонимно. Чтобы начать получчать валентинки нажми \"Хочу валентинки\"",
                         reply_markup=kb.main_kb)
    # if NOTIFICATION:  # Это мне просто чтобы посмотреть насколько народ пользуется ботом
    #     await bot.send_message(1821744447, '+1 user')
    await state.set_state('waiting text')
    await state.update_data(stacy_id=message.get_args())
    if NOTIFICATION:  # Это мне просто чтобы посмотреть насколько народ пользуется ботом
        await bot.send_message(1821744447, '@' + message.from_user.username
                               + ' ' + str(message.from_user.id))
    await save_id(message.from_user.id)


@dp.message_handler(state='*', text=['Поддержать проект💳'])
async def process_donate(message: types.Message):
    await message.answer("🍀🍀🍀\n"
                         "Приятно что тыкнули. Вот номер карты."
                         ": \n2200 2404 6271 3468\n"
                         "Кстати, по вопросам и отзывам можно писать сюда @bryansk_sever111",
                         reply_markup=kb.main_kb)


@dp.message_handler(text=['Хочу валентинку❤️'], state='*')
async def process_start_command(message: types.Message, state: FSMContext):
    link = 't.me/sweetfunnyvalentine_bot?start=' + str(message.from_user.id)
    await message.answer("Вот твоя ссылка\n" + link + '\n' +
                         "Запости куда хочешь. Тот, кто перейдет по ссылке, сможет "
                         "отправить анонимную валентинку тебе ❤️", reply_markup=kb.main_kb)
    if NOTIFICATION:  # Это мне просто чтобы посмотреть насколько народ пользуется ботом
        await bot.send_message(1821744447, 'generated link')


@dp.message_handler(state='waiting text')
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        stacy_id = data['stacy_id']
        await bot.send_message(stacy_id, "Тебе что-то написали:\n" + message.text)
    await message.answer("Ура, отправили валентинку!")
    if NOTIFICATION:  # Это мне просто чтобы посмотреть насколько народ пользуется ботом
        await bot.send_message(1821744447, '+1 user')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


