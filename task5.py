#Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)

from random import randint

n = int(input('Введите число: '))

number = list(range(-n, n + 1))
print(number)

number_2 = number[:]
number_2_length = len(number)

for i in range(number_2_length):
    index = randint(0, number_2_length - 2)
    temp = number_2[i]
    number_2[i] = number_2[index]
    number_2[index] = temp

print(number_2)
