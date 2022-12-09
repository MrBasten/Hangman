from hangmanforplayer import HangManForRusPlayer
from guess import HangmanGuessingRus
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
import os

storage = MemoryStorage()
bot = Bot(token='5508498603:AAG91bL7OyozDlqxNcE4j3of-GGzzoV04aQ')
dp = Dispatcher(bot, storage=storage)
letter = " "
word = " "
hide = " "
count_of_error = 0
answer = " "


class MyState(StatesGroup):
    wait_for_inputs = State()
    success = State()
    not_succsess = State()
    wait_for_inputs_2 = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! \nДавай сыграем в игру?) \nВведите команду /play для начала игры.")


@dp.message_handler(commands=['play'])
async def process_play(message: types.Message):
    global keyboard_play
    keyboard_play = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_play = ["🇷🇺 Выберите язык", "🇬🇧 Choose your language"]
    keyboard_play.add(*buttons_play)
    await message.answer("🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=keyboard_play)


@dp.message_handler(Text(equals="🇷🇺 Выберите язык"))
async def RUS(message: types.Message):
    await message.answer("Выбрана игра на русском", reply_markup=ReplyKeyboardRemove())
    keyboard_RUS = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_RUS = ["Отгадать", "Загадать"]
    keyboard_RUS.add(*buttons_RUS)
    await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?", reply_markup=keyboard_RUS)


@dp.message_handler(Text(equals="Отгадать"))
async def guess(message: types.Message):
    global count_of_error
    global answer
    global hide
    global word
    word = HangManForRusPlayer.rand_word()
    hide = HangManForRusPlayer.hide_word(word)
    await message.answer("ВИСИЛИЦА", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"ваше слово:{hide} .\nВводите по одной букве и не торопитесь, это не смертельная игра. ХАХАХАХАХАХ")
    await MyState.wait_for_inputs.set()


@dp.message_handler(state=MyState.wait_for_inputs)
async def input_from_user(message: types.Message, state: FSMContext):
    global word
    global letter
    global count_of_error
    global hide

    letter = message.text
    hide, answer, count_of_error = HangManForRusPlayer.check_word(
        hide, word, letter, count_of_error)
    if (answer == 'в'):
        await message.answer("Выиграл")
        await message.answer(f"{word}")
        await MyState.success.set()
    elif (answer == 'п'):
        await message.answer("Проиграл")
        await message.answer(f"{word}")
        await MyState.not_succsess.set()
    elif (answer == 'н'):
        await message.answer("Лох, неправильно")
        await message.answer(f"{hide}")
    elif (answer == 'з'):
        await message.answer("Красава!")
        await message.answer(f"{hide}")


@dp.message_handler(Text(equals="Загадать"))
async def make_a_wish(message: types.Message):
    await message.answer("ВИСИЛИЦА")
    await message.answer("Введи скрытые буквы с помощью _. Пример ввода - c_о_о (слово). \nЯ отгадаю любое твоё слово.")
    await MyState.wait_for_inputs_2.set()


@dp.message_handler(state=MyState.wait_for_inputs_2)
async def pop(message: types.Message, state: FSMContext):
    await message.answer("ЪуЪ")
    global word
    global hide
    global count_of_error
    global answer
    global setword
    setword = set()
    word = " "
    hide = message.text
    print(hide)
    i = 0
    count_of_error = 0
    answer = ' '
    sets, hide1, lines = HangmanGuessingRus.Var(hide)
    while(1):
        setword = HangmanGuessingRus.sett(lines, hide)
        if (len(setword) == 1):
            k = setword.pop()
            await message.answer(f"ваше слово {k}")
            await MyState.success.set()
            break
        hide1, word, i, setword = HangmanGuessingRus.Guess(
            hide1, setword, sets)

        await message.answer(f"В слове есть буква {word[i]} на позиции {i+1}?")


@dp.message_handler(Text(equals=f"В слове есть буква {word[i]} на позиции {i+1}?"))
async def ZED(message: types.Message):
    keyboard_ZED = types.ReplyKeyboardMarkup(
        resize_keyboard=True)
    buttons_ZED = ["Да", "Нет"]
    keyboard_ZED.add(*buttons_ZED)
    await message.answer("Сделай свой выбор", reply_markup=keyboard_ZED)


@dp.message_handler(Text(equals="Да"))
async def ZED_1(message: types.Message):
    hide1[i] = word[i]
    setword.add(word)


@dp.message_handler(Text(equals="Нет"))
async def ZED_2(message: types.Message):
    countOfErrors = countOfErrors+1
    sets[i].add(word[i])
    if (countOfErrors == 6):
        print("алгоритм долбаеб")
        exit()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
