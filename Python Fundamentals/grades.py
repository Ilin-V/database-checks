#Список из чисел
numbers_list = [5, 3, 4, 5, 2, 4]
#Сумма
summ = 0
for i in numbers_list:
    summ += i
print(summ)

#Среднее число
average = summ/2
print(float(average))

#Подсчет двоек
count_two = 0
for i in numbers_list:
    if i == 2:
        count_two +=1
print(count_two)

#Максимум
maxim = 0
for i in numbers_list:
    if i > maxim:
        maxim = i
print(maxim)