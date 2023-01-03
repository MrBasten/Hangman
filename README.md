# Проект по курсу "ООП"
![Hangman](https://user-images.githubusercontent.com/69163582/209092220-04ba1647-c567-437f-985d-b67cc6f7938b.jpg)

<p align="center">
   <img src="https://img.shields.io/badge/python-3.8.10-blue" alt="Python Version">
   <img src="https://img.shields.io/badge/aiogram-2.23.1-green" alt="Aiogram Version">
   <img src="https://img.shields.io/badge/Levenshtein-0.20.9-orange" alt="Levenshtein Version">
</p>

## Тема проекта: "Реализация игры Hangman в telegram-боте"
В рамках проекта разработан алгоритм для игры Hangman, основанный на [расстоянии Левенштейна](https://habr.com/ru/post/676858/) и telegram-бот, которого можно "попросить" либо поиграть с вами, либо отгадать слово, которое придумаете вы.

## Зоны ответственности разработчиков (М8О-208Б-21)

[**Стенин К.А.**](https://github.com/MrBasten)
- Оформление гитхаба
- Разработка бота

[**Чубуков А.В.**](https://github.com/Mrak0bEss)
- Разработка алгоритма  

## Инструкция
1. Для запуска нужно поместить всё части проекта в одну папку и запустить файл с названием  **telegram_bot.py**
2. Перейти в telegram и найти бота ( https://t.me/hangman27_bot )
3. Ввести команду "/start"

## Пример работы
1. Запуск игры для отгадывания слова

![Screenshot from 2023-01-03 17-54-02](https://user-images.githubusercontent.com/69163582/210391035-31790018-3119-4eb1-bcd8-632607b797d8.png)

После вывод слова алгоритмом его надо начать отгадывать, вводя по одной букве
В случае успеха:

![Screenshot from 2023-01-03 17-57-04](https://user-images.githubusercontent.com/69163582/210391408-671ded86-2718-4f5d-b163-468edeb390c7.png)

В случае неудачи:

![Screenshot from 2023-01-03 17-57-20](https://user-images.githubusercontent.com/69163582/210391481-2b9df9df-3c37-459c-8a3b-c41b1e88553d.png)

Попыток ограниченное количество, если слово угадано до окончания счётчика:

![Screenshot from 2023-01-03 17-58-03](https://user-images.githubusercontent.com/69163582/210391826-df25d0b5-939e-4b11-845e-a8371d159948.png)

Если же счётчик попыток закончился, то выводится следующее сообщение:

![image](https://user-images.githubusercontent.com/69163582/210397069-4a39799f-fa73-48f4-9b1a-262f56c99d33.png)

2. Запуск игры для загадывания слова

![image](https://user-images.githubusercontent.com/69163582/210398715-21634381-1463-4cfb-bdd2-8b881b32a99a.png)

После зауска игры алгоритм нам будет выводить буквы, которые могут быть частью этого слова, а вам нужно отвечать да/нет. Если да, то алгоритм переходит на следующую позицию, если нет, то алгоритм предлагает следующий вариант буквы:

![image](https://user-images.githubusercontent.com/69163582/210404457-354890d8-297d-42aa-be69-31045546cb0c.png)

У бота также есть только лишь несколько попыток, после исчерпания которых выводится следющее сообщение:

![Screenshot from 2023-01-03 19-24-41](https://user-images.githubusercontent.com/69163582/210398453-eab8b825-371a-41be-b1e6-6475b1643dc4.png)







