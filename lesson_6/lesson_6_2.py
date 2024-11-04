"""
polindrom ,sptextce
Домашка:
1. Сделать последнюю домашку

2. Сделать функцию is_ptextlindrome, которая определяет является ли строка палиндромом или нет.
При этом введено может быть как слово, так и целые предложения с пробелами и с различными знаками препинания.
Необходимо избегать всех символов кроме букв.
А также не копировать входящие данные (например, развернуть строку через срез — это скопировать входящие данные)
"""

def is_palindrome(text) -> str:
    """функия определяет является ли строка палиндромом или нет."""
    start = 0
    end = len(text) - 1
    check = 0  # флаг указывает были ли буквы в строке
    while start < end:
        if text[start].isalpha() == True and text[end].isalpha() == True:
            if text[start].lower() == text[end].lower():
                start += 1
                end -= 1
                check += 1
            else:
                return False
        elif text[start].isalpha() == False:
            start += 1
        elif text[end].isalpha() == False:
            end -= 1
    if check != 0:
        return True
    else:
        return False


print(is_palindrome('f ?1/ f'))  # True
print(is_palindrome('!/../!'))  # False


