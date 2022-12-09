# Вислелица с возможностью загадывания и отгадывания 
Отгадывание основан на алгоритме Левенштейна, и соответсвующих библиотеках - fuzzywuzzy и Levenshtein 

Работа реализована на двух языках - английский и русский, пример ввода -
```
PS C:\Users\123ko\desktop> python hangman.py
Введите язык/Enter your lang. (рус\eng)
рус
Выбрана игра на русском
отгадать слово или загадать? введие о\з
о
В и с е л и ц а
шо__тур
р
Такая буква есть!
шо__тур
т
Такая буква есть!
шо__тур
к
Ошибка!

     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------

шо__тур
у
Такая буква есть!
шо__тур
з
Ошибка!

     ------
     |    |
     |    O
     |    |
     |
     |
     |
    ----------

шо__тур
й
Ошибка!

     ------
     |    |
     |    O
     |   /|
     |
     |
     |
    ----------

шо__тур
п
Такая буква есть!
шоп_тур
а
Ошибка!

     ------
     |    |
     |    O
     |   /|\
     |
     |
     |
    ----

шоп_тур
е
Ошибка!

     ------
     |    |
     |    O
     |   /|\
     |   /
     |
     |
    ----

шоп_тур
и
Ошибка!

     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
     |
    ----

шоп_тур
Игрок проиграл
Слово - шоп-тур
Хотите продолжить? (д/н)
н
PS C:\Users\123ko\desktop> 
```
english - 
```
PS C:\Users\123ko\desktop> python hangman.py
Введите язык/Enter your lang. (рус\eng)
eng
Plying in english
guess a word or make a guess? enter o\m
o
H a n g m a n
sail___t
e
Error!

     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------

sail___t
d
Error!

     ------
     |    |
     |    O
     |    |
     |
     |
     |
    ----------

sail___t
t
There is such a letter!
sail___t
q
Error!

     ------
     |    |
     |    O
     |   /|
     |
     |
     |
    ----------

sail___t
i
There is such a letter!
sail___t
h
Error!

     ------
     |    |
     |    O
     |   /|\
     |
     |
     |
    ----

sail___t
z
Error!

     ------
     |    |
     |    O
     |   /|\
     |   /
     |
     |
    ----

sail___t
n
Error!

     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
     |
    ----

sail___t
Player lose
Word - sailboat
Want countinue? (y/n)
n
```
Алгоритм загадывания прост, рандомное слово из словаря шифруется и игроку предлагается написать символ, который подается на проверку наличия в слове.
```
print("В и с е л и ц а")
        print(hide_word)
        count_of_error=0
        list1=[None]*len(word)
        list2=[None]*len(hide_word)
        while count_of_error<6:
            s=input()
            for i in range(len(word)):
          #  print(i)
                list1[i]=word[i]
                list2[i]=hide_word[i]
            if s in word:
                print('Такая буква есть!')
                for i in range(len(word)):
                        if list1[i] == s:
                            list2[i] = s
                hide_word=''.join(list2)
                print(hide_word)
            else:
                print('Ошибка!')
                count_of_error+=1
                PrintHang.hang(count_of_error)
                hide_word=''.join(list2)
                print(hide_word)
            if list1 == list2:
                print('Игрок выйграл!')
                break
        if count_of_error == 6:
            print('Игрок проиграл')
            print('Слово - '+ word)
```
Алгоритм отгадывания беерт все слова с такими же открытыми буквами и длинной слов и проверяет на бОльшее соответсвие через алгоритм Левенштейна.
```
 hide=[None]*len(hide1)
        for i in range(len(hide1)):
            #  print(i)
            hide[i]=hide1[i]
        #print(hide)     
        with open('singular_and_plural.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
        setword=set()
        max=0
        min=0
        countOfErrors=0
        while (countOfErrors<6):
            for wrds in lines:
                if len(wrds)==len(hide) and Sravnenie.chek(hide,wrds):
                    if fuzz.ratio(hide,wrds)>max:
                        setword=set()
                        setword.add(wrds)
                        min=distance(wrds,hide)
                        max =fuzz.ratio(hide,wrds)
                    if fuzz.ratio(hide,wrds)==max:
                        setword.add(wrds)
            if len(setword)==1:
                print(setword.pop())
                break
            elif len(setword)==0:
                print("Такого слова нет в словаре(")
                break
            else:
               # print(setword)
                for x in setword:
                   # print(x)
                    while(True):
                        ind=random.randint(0,len(x)-1)
                        if hide[ind]=='_':
                            break
                    print('В слове есть такая буква? (напишите д/н)')
                    print(x[ind])
                    answer=''
                    answer=input()
                    if (answer == 'д'):
                        hide[ind]=x[ind]
                        break
                    else:
                        countOfErrors=countOfErrors+1
                        PrintHang.hang(countOfErrors)
                        if countOfErrors==6:
                            print('Бездушная машина не смогла отгадать слово')
                            break

```

