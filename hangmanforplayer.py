import random


class HangManForRusPlayer:
   # выбор рандомного слова из файла
    def rand_word():
        with open('russian_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        i = random.randint(0, len(lines))
        return lines[i]
    # генерация слова со спрятанными буквами

    def hide_word(s):
        if (len(s) >= 7):
            count = 5
        elif (len(s) >= 5):
            count = 3
        else:
            count = 2
        # hide_string='___'
        list1 = [None]*len(s)
        list2 = [None]*len(s)
        for i in range(len(s)):
          #  print(i)
            list2[i] = s[i]

        ban = set()
        for i in range(len(s)):
            list1[i] = '_'
        for i in range(count):
            while(True):
                j = random.randint(0, len(s)-1)
                if j not in ban:
                    ban.add(j)
                    break
            list1[j] = list2[j]
            hide_string = ''.join(list1)
        return hide_string

    def check_word(hide_word, word, s, count_of_errors) -> tuple:
        list1 = [None]*len(word)
        list2 = [None]*len(hide_word)
        for i in range(len(word)):
          #  print(i)
            list1[i] = word[i]
            list2[i] = hide_word[i]
        if s in word:

            for i in range(len(word)):
                if list1[i] == s:
                    list2[i] = s

            hide_word = ''.join(list2)
            answ = ('з')
           # print(hide_word)

        else:

            hide_word = ''.join(list2)
            answ = ('н')
            count_of_errors = count_of_errors+1
            if (count_of_errors == 6):
                answ = 'п'
           # print(hide_word)
        if list1 == list2:
            answ = ('в')
        return hide_word, answ, count_of_errors


class HangManForEngPlayer(HangManForRusPlayer):
    def rand_word():
        with open('english_nouns.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        i = random.randint(0, len(lines))
        return lines[i]

    def process_of_game(word, hide_word):
        print("H a n g m a n")
        print(hide_word)
        count_of_error = 0
        list1 = [None]*len(word)
        list2 = [None]*len(hide_word)
        while count_of_error < 6:
            s = input()
            for i in range(len(word)):
              #  print(i)
                list1[i] = word[i]
                list2[i] = hide_word[i]
            if s in word:
                print('There is such a letter!')
                for i in range(len(word)):
                    if list1[i] == s:
                        list2[i] = s
                hide_word = ''.join(list2)
                print(hide_word)
            else:
                print('Error!')
                count_of_error += 1
                hide_word = ''.join(list2)
                print(hide_word)
            if list1 == list2:
                print('Player win!')
                break
        if count_of_error == 6:
            print('Player lose')
            print('Word - ' + word)
  # ugadivanie
