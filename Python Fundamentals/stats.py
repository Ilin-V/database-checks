text = input("Введите слово: ")
def count_letters(text: str) -> dict:
    dictionary = {}
    for i in text:
        letter = i.lower()
        if letter.isalpha():
            if letter not in dictionary:
                dictionary[i] = 1
            else :
                dictionary[i] +=1
    return dictionary
result = count_letters(text)
print(result)