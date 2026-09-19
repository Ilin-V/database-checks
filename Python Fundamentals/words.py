words = input("Введите строку: ")
text = words.split()
#Сколько слов
count_words = 0
for i in text:
    count_words += 1
print(count_words)

#Самое длинное слово
length = ""
for i in text:
    if len(length) < len(i):
        length = i
print(length)

#Cтроку в нижнем регистре
print(words.lower())