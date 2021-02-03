'''
Давайте начнем с несложной задачи. Ваша цель написать программу (скрипт), которая
будет запускаться из командной строки. Программа принимает в качестве аргумента строку, состоящую из цифр.
Гарантируется, что других символов в переданном параметре нет и на вход всегда подается не пустая строка.
Программа должна вычислить сумму цифр из которых состоит строка и вывести полученный результат на печать в стандартный вывод.

Примеры работы программы:

1234
$ python solution.py 12345
15
$ python solution.py 160438521039
42
Считать переданный параметр можно с помощью модуля стандартной библиотеки sys:

123
import sys

digit_string = sys.argv[1]
Выполнение этого кода, создаст переменную digit_string, значением которой будет строка, переданная в параметре при запуске
вашей программы. Более подробно о модуле sys и передаче параметров в скрипт вы можете прочитать в документации к модулю sys.

Файл с программой должен называться solution.py. После написания и отладки вашего решения, вам необходимо загрузить файл solution.py на платформу для проверки.
'''

# Ответ:

import sys

x = sys.argv[1]

def sum(x):
    digit_string = 0
    for i in x:
        i = int(i)
        digit_string += i
    print(digit_string)
sum(x)

# python3 solution.py 12345
