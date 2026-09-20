#Меню
def menu():
    print("добавить / обновить")
    print("найти по имени")
    print("показать все")
    print("выход")
    action = input("Что хотите выбрать: ")
    return action
#Словарь
phonebook = {"Вадим" : "+7 937 395 94 60"}
#Цикл
while True:
    action = menu()
    #Добавить/обновить
    if action.lower() == "добавить":
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        phonebook[name] = number
        print(phonebook)
    elif action.lower() == "обновить":
        print(phonebook)
        name = input("Введите имя: ")
        number = input("Введите номер: ")
        phonebook[name] = number
        print(phonebook)
    #Найти по имени
    elif action.lower() == "найти по имени" or action.lower() == "найти":
        print(phonebook)
        name = input("Чей номер хотите найти?: ")
        if name in phonebook:
            phone = phonebook[name]
            print(name)
        else:
            print("Контакта нет")
    #Показать все
    elif action.lower() == "показать все" or action.lower() == "показать":
        print(phonebook)
    #Выход
    elif action.lower() == "выход":
        print("Вы вышли!")
        break
    print()