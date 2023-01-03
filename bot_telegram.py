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
rnd = True
sets = [set() for _ in range(5000)]
i = 0
lines = {None}
hide1={None}
keyboard_RUS=' '

#Состаяния для fsm в aiogram
class MyState(StatesGroup):
    wait_for_inputs = State()
    success = State()
    not_succsess = State()
    wait_for_inputs_2 = State()
    check = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! \nДавай сыграем в игру?) \nВведите команду /play для начала игры.")


@dp.message_handler(commands=['play'])
async def process_play(message: types.Message):
    global keyboard_play
    global keyboard_RUS
    await message.reply("Напишите, Отгадать или Загадать.")
    await MyState.success.set()
#Определение режима игры, загадывание или отгадывание
@dp.message_handler(state=MyState.success)
async def input_from_user(message: types.Message, state: FSMContext):
    if (message.text == "Отгадать"):
        global count_of_error
        global answer
        global hide
        global word
        word = HangManForRusPlayer.rand_word()
        hide = HangManForRusPlayer.hide_word(word)
        await message.answer("ВИСИЛИЦА", reply_markup=ReplyKeyboardRemove())
        await message.answer(f"ваше слово:{hide} .\nВводите по одной букве и не торопитесь, это не смертельная игра. ХАХАХАХАХАХ")
        await MyState.wait_for_inputs.set()
    elif(message.text== "Загадать"):
        await message.answer("ВИСИЛИЦА")
        await message.answer("Введи скрытые буквы с помощью _. Пример ввода - c_о_о (слово). \nЯ отгадаю любое твоё слово.")
        await MyState.wait_for_inputs_2.set()
    else:
        await MyState.success.set()

#если выбрано отгадывание то в работу идет этот алгоритм.
#игрок подает возможные буквы, и в зависимости от их наличия, поражения или победы выводится результат
@dp.message_handler(state=MyState.wait_for_inputs)
async def input_from_user(message: types.Message, state: FSMContext):
    global word
    global letter
    global count_of_error
    global hide
    global keyboard_RUS
    letter = message.text
    hide, answer, count_of_error = HangManForRusPlayer.check_word(
        hide, word, letter, count_of_error)
    if (answer == 'в'):
        await message.answer("Выиграл")
        await message.answer(f"{word}")
        await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?\nВведи Отгадать или Загадать")
        await MyState.success.set()
    elif (answer == 'п'):
        await message.answer("Проиграл")
        await message.answer(f"{word}")
        await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?\nВведи Отгадать или Загадать")
        await MyState.success.set()
    elif (answer == 'н'):
        await message.answer("Лох, неправильно")
        await message.answer(f"{hide}")
    elif (answer == 'з'):
        await message.answer("Красава!")
        await message.answer(f"{hide}")

#режим загадывания
#игрок вводит маску слова, алгоритм находит все ближайшие по Левенштейну слова и дает на проверку буквы
#игрок одобряет их или же отклоняет
@dp.message_handler(Text(equals="Загадать"))
async def make_a_wish(message: types.Message):
    await message.answer("ВИСИЛИЦА")
    await message.answer("Введи скрытые буквы с помощью _. Пример ввода - c_о_о (слово). \nЯ отгадаю любое твоё слово.")
    await MyState.wait_for_inputs_2.set()


@dp.message_handler(state=MyState.wait_for_inputs_2)
async def pop(message: types.Message, state: FSMContext):
    global word
    global hide
    global count_of_error
    global answer
    global setword
    global rnd
    global sets
    global lines
    global i
    global hide1
    if (rnd):
        setword=set()
        word = " "
        hide = message.text
        print(hide)
        i = 0
        count_of_error = 0
        answer = ' '
        hide1, lines = HangmanGuessingRus.Var(hide)
    else:
        answ=message.text
        if(answ == 'Да'):
            hide1[i] = word[i]
            hide=''.join(hide1)
            setword.add(word)
        if(answ == 'Нет'):
            count_of_error = count_of_error+1
            sets[i].add(word[i])
            if (count_of_error == 6):
                
                await message.answer("Бот не смог отгадать слово.")
                await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?\nВведи Отгадать или Загадать")
                await MyState.success.set()
                exit()
    
    setword = HangmanGuessingRus.sett(lines, hide)
    
    if (len(setword) == 0):
        await message.answer("Бот не смог отгадать слово.")
        await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?\nВведи Отгадать или Загадать")
        await MyState.success.set()
    else:   
        if (len(setword) == 1):
            k=setword.pop()
            await message.answer(f"Ваше слово {k}")
            #print(setword.pop())
            await message.answer("Хочешь загадать слово мне или я проверю твою эрудицию?\nВведи Отгадать или Загадать")
            await MyState.success.set()
        else:
            hide1, word, i, setword = HangmanGuessingRus.Guess(
                hide1, setword, sets)
            rnd = False
            await message.answer(f"В слове есть буква {word[i]} на позиции {i+1}?")
            #@dp.message_handler(Text(equals=f"В лове есть буква {word[i]} на позиции {i+1}?"))
            await MyState.wait_for_inputs_2.set()            
    
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
