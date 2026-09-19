#Список из чисел
numbers_list = []

while True:
    numbers = input("Введите цифр или (стоп): ")
    if numbers.lower() == "стоп":
        break
    numbers_list.append(int(numbers))

#Сумма
def sum(numbers_list):
    summ = 0
    for i in numbers_list:
        summ += i
    return summ
total_sum = sum(numbers_list)

#Среднее число
def aver(summ,numbers_list):
    average = summ/ len(numbers_list)
    return average
mid_num = aver(total_sum, numbers_list)

#Сколько двоек
def count():
    count_two = 0
    for i in numbers_list:
        if i == 2:
            count_two +=1
    return count_two
count_num = count()

#Максимум
def max():
    maxim = 0
    for i in numbers_list:
        if i > maxim:
            maxim = i
    return maxim
max_num = max()

#Вывод
print(f"Среднее число: {float(mid_num)}")
print(f"Cколько двоек: {count_num}")
print(f"Mаксимум: {max_num}")