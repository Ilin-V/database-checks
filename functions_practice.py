#1 функция
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False
#2 функция
def clamp(x, low, high):
    if x <low:
        return low
    elif x>low:
        return high
    else:
        return x
#3 функция
def unique_words(text: str) -> list:
    my_list = []
    for i in text.lower().split():
        if i not in my_list:
            my_list.append(i)
    return my_list
#Выводы
print(is_even(4))
print(clamp(15,0,10))
print(unique_words("Hi hi BYE"))