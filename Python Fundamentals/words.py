words = input("Введите строку: ")
text = words.split()
#Сколько слов
def words_many(text):
    count_words = 0
    for i in text:
        count_words += 1
    return count_words
count_words = words_many(text)

#Самое длинное слово
def len_word(text):
    length = ""
    for i in text:
        if len(length) < len(i):
            length = i
    return length
length = len_word(text)

#Вывод
print(f"Сколько слов: {count_words}")
print(f"Самое длинное слово: {length}")
#Cтроку в нижнем регистре
print(words.lower())