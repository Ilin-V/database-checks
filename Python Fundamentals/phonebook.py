#Меню
def menu():
    print("Добавить / обновить")
    print("Найти по имени")
    print("Показать все")
    print("Выход")
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
    if action.lower() == "найти по имени" or action.lower() == "найти":
        print(phonebook)
        name = input("Чей номер хотите найти?: ")
        if name in phonebook:
            name = phonebook[name]
            print(name)
        else:
            print("Контакта нет")
    #Показать все
    if action.lower() == "показать все" or action.lower() == "показать":
        print(phonebook)
    #Выход
    if action.lower() == "выход":
        print("Вы вышли!")
        break
    print()