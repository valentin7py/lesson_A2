"""
polindrom ,sptextce
Домашка:
1. Сделать последнюю домашку

2. Сделать функцию is_ptextlindrome, которая определяет является ли строка палиндромом или нет.
При этом введено может быть как слово, так и целые предложения с пробелами и с различными знаками препинания.
Необходимо избегать всех символов кроме букв.
А также не копировать входящие данные (например, развернуть строку через срез — это скопировать входящие данные)
Aleander:
Выглядит сложно, если честно. Можно очень сильно упростить. Сможешь сделать проще?)
"""


def is_palindrome(text) -> str:
    """функия определяет является ли строка палиндромом или нет."""
    start = 0
    end = len(text) - 1
    start_letter = text[start].lower()
    end_letter = text[end].lower()
    while start < end:
        if not start_letter.isalpha() :
            start += 1
        if not end_letter.isalpha():
            end -= 1
            continue
        if start_letter == end_letter:
            start += 1
            end -= 1
            continue
        return False
    return True


print(is_palindrome('ra.ж ar'))  # True
print(is_palindrome('папа'))  # False
print(is_palindrome(' a,b a/'))  # True
print(is_palindrome('Б/.,е1243л хл еб.'))  # True
