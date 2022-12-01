#Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#Пример:
#- Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
# Необходимо сложить все значения словаря и вывести сумму на экран. (словарь=список)

n = int(input('Введите число: '))
def in_list(n):
    list = []
    for i in range (1, n+1):
        list.append((1+1/i)**i)
    return list

def sum(list):
    sum=0
    for i in range (len(list)):
        sum=sum + list[i]
    return sum

list = in_list(n)
print(list)
result = sum(list)
print(result)
