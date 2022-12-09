from Levenshtein import distance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import random

from printhang import PrintHang
from equal import Sravnenie


class HangmanGuessingRus:
    def sett(lines, hide):
        setword = set()
        max = 0
        min = 0

        for wrds in lines:
            if len(wrds) == len(hide) and Sravnenie.chek(hide, wrds):
                if fuzz.ratio(hide, wrds) > max:
                    setword = set()
                    setword.add(wrds)
                    min = distance(wrds, hide)
                    max = fuzz.ratio(hide, wrds)
                if fuzz.ratio(hide, wrds) == max:
                    setword.add(wrds)
        return setword

    def Guess(hide, setword, sets) -> tuple:
        for i in setword:
            print(i)
        ind = 0
        if len(setword) == 1:
            return hide, ' ', ind, setword

        else:
            # print(setword)
            x = ' '
            # print(x)
            while (1):
                x = setword.pop()
                for i in range(len(x)):

                    if (x[i] not in sets[i]):
                        ind = i

                        if (hide[ind] == '_'):

                            return hide, x, ind, setword

        return hide, x, ind, setword

    def Var(hide) -> tuple:

        hide1 = [None]*len(hide)
        for i in range(len(hide)):
            #  print(i)
            hide1[i] = hide[i]
        # print(hide)
        with open('singular_and_plural.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        return hide1, lines
    """
                print('В слове есть такая буква? (напишите д/н)')

                answer=''
                answer=input()
                if (answer == 'д'):
                    hide[ind]=x[ind]
                    break
                else:
                    countOfErrors=countOfErrors+1
                    PrintHang.hang(countOfErrors)
                    """
    # print(hide)


class HangmanGuessingEng:
    def Guess(hide1):
        hide = [None]*len(hide1)
        for i in range(len(hide1)):
            #  print(i)
            hide[i] = hide1[i]
        # print(hide)
        with open('english_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        setword = set()
        # print(1);
        max = 0
        min = 0
        countOfErrors = 0
        while (countOfErrors < 6):
            for wrds in lines:
                if len(wrds) == len(hide) and Sravnenie.chek(hide, wrds):
                    if fuzz.ratio(hide, wrds) > max:
                        setword = set()
                        setword.add(wrds)
                        min = distance(wrds, hide)
                        max = fuzz.ratio(hide, wrds)
                    if fuzz.ratio(hide, wrds) == max:
                        setword.add(wrds)
            if len(setword) == 1:
                print(setword.pop())
                break
            elif len(setword) == 0:
                print("There is no a such word in library(")
                break
            else:
               # print(setword)
                for x in setword:
                    # print(x)
                    while (True):
                        ind = random.randint(0, len(x)-1)
                        if hide[ind] == '_':
                            break
                    print('Is there such a letter in the word? (Enter y/n)')
                    print(x[ind])
                    answer = ''
                    answer = input()
                    if (answer == 'y'):
                        hide[ind] = x[ind]
                        break
                    else:
                        countOfErrors = countOfErrors+1
                        PrintHang.hang(countOfErrors)
                        if countOfErrors == 6:
                            print('The soulless machine could not guess the word')
                            break
