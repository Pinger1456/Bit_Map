"""Сообщение в виде битовой карты, (c) Эл Свейгарт al@inventwithpython.com
Отображает текстовое сообщение в соответствии с указанной битовой картой.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: крошечная, для начинающих, графика"""

import sys
import config
# (!) Попробуйте заменить это многострочное строковое значение на любое
# другое изображение. Вверху и внизу строки расположено 68 точек:
# (Можете также скопировать и вставить это строковое значение из
# https://inventwithpython.com/bitmapworld.txt)


print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')

# Проверка на пустое сообщение. Если оно пустое, завершить программу.
if message == '':
    sys.exit()

# Проходим в цикле по всем строкам битовой карты:
for line in config.BIT_MAP.splitlines():
    # Проходим в цикле по всем символам строки:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Пробелы в битовой карте остаются пустыми:
            print(' ', end='')
        else:
            # Выводим символ сообщения:
            print(message[i % len(message)], end='')

    print()  # Переход на новую строку.
