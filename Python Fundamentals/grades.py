#Список из чисел
numbers_list = []

while True:
    numbers = input("Введите цифр или (стоп): ")
    if numbers.lower() == "стоп" :
        print("Ошибка деления на ноль")
        break
    numbers_list.append(int(numbers))
#Сумма
def suma(numbers_list):
    summ = 0
    for i in numbers_list:
        summ += i
    return summ
total_sum = suma(numbers_list)
#Среднее число
def aver(summ,numbers_list):
    average = summ / len(numbers_list)
    return average
mid_num = aver(total_sum, numbers_list)
#Сколько двоек
def count(numbers_list):
    count_two = 0
    for i in numbers_list:
        if i == 2:
            count_two +=1
    return count_two
count_num = count()
#Максимум
def maxu(numbers_list):
    maxim = 0
    for i in numbers_list:
        if i > maxim:
            maxim = i
    return maxim
max_num = maxu()
#Вывод
print(f"Среднее число: {float(mid_num)}")
print(f"Cколько двоек: {count_num}")
print(f"Mаксимум: {max_num}")