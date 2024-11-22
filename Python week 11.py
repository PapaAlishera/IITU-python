""" Задание 1
Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором. """

list1 = input().split(' ')
list2 = input().split(' ')

for i in list1:
    if i not in list2:
        print(i)

""" Задание 2
Распечатайте список файлов в указанном каталоге. """

import os

directory = input()

try:
    files = os.listdir(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
except Exception:
    print(f"Произошла ошибка: {Exception}")

""" Задание 3
Сложите цифры целого числа. """

chislo = input()
num = 0
for i in range(len(chislo)):
    num += int(chislo[i])
print(num)

""" Задание 4
Подсчитайте количество раз, когда символ встречается в строке. """

stroka = input()
sim = input()
kol = 0
for i in range(len(stroka)):
    if sim == stroka[i]:
        kol += 1
print(kol)

""" Задание 5
Поменяйте местами значения переменных. """

a = input()
b = input()

a, b = b, a

print(a)
print(b)

""" Задание 6
Используйте анонимную функцию для извлечения чисел, кратных 15, из списка. """


num = [10, 15, 30, 45, 60, 7, 22, 23, 90]

krat15 = list(filter(lambda x: x % 15 == 0, num))

print(krat15)

""" Задание 7
Нужно проверить, все ли числа в последовательности уникальны. """

num = input().split(' ')

if len(num) == len(set(num)):
    print("Уникальны")
else:
    print("Не уникальны")
