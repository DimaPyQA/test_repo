#Дан список. Нужно вывести '2-4' строка,  5 6 - числа, '7-10' - строка

digits = [2,4,5,6,7,10]     2-4, 5, 6, 7-10
# index = 0
result = []
result_x = []

for digit in digits:
    if len(result_x) == 0:
        result_x += [digit]
    else:
        result_x += [digit]
        if result_x[-1] - result_x[-2] == 1:
            result += [result_x[-2]]
            result += [result_x[-1]]
        else:
            str1 = f'{result_x[-2]} - {result_x[-1]}'
            result += [str1]

print(result)