

from printhang import PrintHang
from guess import HangmanGuessingEng
from guess import HangmanGuessingRus
from player import Player
import random
import sys
from hangmanforplayer import HangManForRusPlayer

"""
def algorintm_gess_word(target_word : str, curent_letter : str, correct_leters : list = [], incorect_letters : list = [], number_of_penalties : int = 0) -> tuple:
    if curent_letter in correct_leters:
        number_of_penaltis += 1
        #if number_of_penalties >= 3:
        #    return [], [], number_of_penalties
        return correct_leters, incorect_letters, number_of_penalties
        
    if curent_letter in target_word:
        correct_leters.append(curent_letter)
        return correct_leters, incorect_letters, number_of_penalties
    
    incorect_letters.append(curent_letter)
    return correct_leters, incorect_letters, number_of_penalties

a, b, c = algorintm_gess_word('abc', 't')
print(a, b, c)
exit()
"""


N = Player()
while (N.lang != 'рус' and N.lang != 'eng'):
    print('Неверный ввод языка(Lang error)')
    N.lang = input()
refresh = 'д'
functoin = ''
while (refresh == 'д' or refresh == 'y'):
    if (N.lang == 'рус'):
        print("Выбрана игра на русском")
        print('отгадать слово или загадать? введие о\з')
        function = input()
        if function == 'о':
            word = HangManForRusPlayer.rand_word()
            hide = HangManForRusPlayer.hide_word(word)
            print("В и с е л и ц а")

            count_of_error = 0
            answ = ' '
            while (1):
                print(hide)
                s = input()
                hide, answ, count_of_error = HangManForRusPlayer.check_word(
                    hide, word, s, count_of_error)
                if (answ == 'в'):
                    print("win")
                    break
                elif (answ == 'п'):
                    print("lose")
                    print(word)
                    break
                elif (answ == 'н'):
                    print("ошибка")

        elif function == 'з':
            print('введите скрытые элементы с помощью _. Прмер ввода - c_о_о (слово).')
            hide = input()
            i = 0
            word = ""
            countOfErrors = 0
            answer = ' '
            sets, hide1, lines = HangmanGuessingRus.Var(hide)
            while(1):
                setword = HangmanGuessingRus.sett(lines, hide1)
                hide1, word, i, setword = HangmanGuessingRus.Guess(
                    hide1, setword, sets)
                if (len(setword) == 1):
                    print("Ваше слово :")
                    print(setword.pop())
                    break
                else:
                    print('В слове есть такая буква на позиции ',
                          i+1, ' ? (напишите д/н)')
                    print(word[i])
                    answer = ''
                    answer = input()
                    if (answer == 'д'):
                        hide1[i] = word[i]
                        setword.add(word)
                    else:
                        countOfErrors = countOfErrors+1
                        sets[i].add(word[i])
                        if (countOfErrors == 6):
                            print("алгоритм долбаеб")
                            break

            print('Хотите продолжить? (д/н)')
            refresh = input()
    elif (N.lang == 'eng'):

        print("Plying in english")
        '''
        print('guess a word or make a guess? enter o\m')
        function=input()
        if function == 'o':
            word = HangManForEngPlayer.rand_word()
            hide = HangManForEngPlayer.hide_word(word)
            HangManForEngPlayer.process_of_game(word,hide)
        elif function =='m':
            print('Enter the hidden elements using _. An example of input is w_rd (word).')
            hide=input()
            HangmanGuessingEng.Guess(hide)
        print('Want countinue? (y/n)')
        refresh = input()
        '''
# retutn ([correct leters], [incorect leters])
