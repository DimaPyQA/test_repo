#Task 1 - Напишите программу, которая принимает на вход список чисел и выводит сумму всех его элементов
# raw_numbers = input('Input numbers: ')
# sum_number = 0
# for n in raw_numbers:
#     if n == ',':
#         pass
#     else:
#         number = int(n)
#         sum_number += number
# print(sum_number)

#Task 2 - Напишите программу, которая принимает на вход список чисел и выводит сумму всех его элементов, исключая максимальное число
raw_numbers = input('Через запятую введите список чисел: ')
int_numbers = []

for n in raw_numbers:
    if n == ',':
        pass
    else:
        number = int(n)
        int_numbers += [number]

indexes = range(len(int_numbers))
print(int_numbers)
print(indexes)

sum_number = 0

for i in indexes:
    if i == indexes[-1]:
        pass
    else:
        sum_number += int_numbers[i]
print(sum_number)