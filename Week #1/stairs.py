'''
Это задание чуть сложней предыдущего и потребует от вас размышлений. Необходимо написать скрипт, который
«нарисует» (выведет на консоль) лестницу. Количество ступенек в лестнице передается скрипту в качестве параметра.
Гарантируется, что на вход подаются только целые числа > 0.﻿ Чтение данных нужно произвести способом, аналогичным тому, что
описан в предыдущем задании. Ступени должны отображаться с помощью символа решетки  "#" и пробелов. Пример работы скрипта:

На что  обратить внимание? Вывод должен содержать только пробелы и символ "#". Первая строка вывода не должна быть пустой.
Строки вывода лестницы не должны содержать лишних пробелов в начале и конце строки. Допускается наличие пустой строки после
вывода последней строки, содержащей ступени. Например так:
'''

# Ответ:
# python3 python.py 4

import sys

x = int(sys.argv[1])
a = 1

for i in range(x):
    y = x - a -1
    if a != x:
        print(' '* y, '#' * a)
    else:
        print('#' * x)
    a += 1
