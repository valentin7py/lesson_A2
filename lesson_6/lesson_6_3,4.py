"""
3.+ Функции на проверку имени, возраста и совет паспорт должны возвращать None
(иначе говоря, ничего не должны возвращать),
если не было ошибок или нет советов

4. Сделать функцию, которая генерирует случайное число от 0 до 10,
и в бесконечном цикле просит пользователя угадать это число, если пользователь ввёл имя и возраст корректные"""
import random


def remove_space(name: str) -> str:
    """Удаляет пробелы. Буквально понял 6 пункт. Наверно лучше в input_data() реализовать через strip() """
    return name.strip()


def check_name(name: str) -> str:
    """Проверкака имени"""
    if not name:
        return "Ошибка: пустое имя."
    elif len(name) < 3:
        return 'Ошибка: В имени должно быть минимум 3 символа.'
    elif name.count(' ') > 1:
        return "Ошибка: В имени между буквами допускается только 1 пробел."
    return name


def check_age(age: int) -> int:
    """Проверкака возраста"""
    if type(age) != int:
        return "Ошибка : неверный тип данных"
    elif age <= 0:
        return 'Ошибка: возраст не можеть быть равен или меньше 0'
    elif age < 14:
        return 'Ошибка: Минимальный возраст — 14 лет.'
    elif age > 111:
        return 'Ты кто?'
    return age


def input_data():
    """Ввод данных"""
    while True:
        name = remove_space(input('Введите имя: '))
        age = int(input('Введите возраст: '))

        if check_name(name) == name and check_age(age) == age:
            break
        if check_name(name) != name:
            print(check_name(name))
        if check_age(age) != age:
            # 3 if для того что бы выводило обе ошибки. из-за этого в програме 3 print.
            print(check_age(age))
    return name, age


def rez_func(name: str, age: int) -> str:
    """Результирующая функция"""
    default_text = f'Привет,{name.title()}! Тебе {age} лет.'
    rez_text = ''
    if 16 <= age <= 17:
        rez_text += default_text
        rez_text += 'Нужно не забыть получить первый паспорт'
    elif 25 <= age <= 26:
        rez_text += default_text
        rez_text += 'Не забудь заменить паспорт по достижению 25 лет.'
    elif 45 <= age <= 46:
        rez_text += default_text
        rez_text += 'Не забудь заменить паспорт по достижению 45 лет.'
    if len(rez_text) != 0:
        return print(rez_text)


def random_number():
    print('Давай поиграем!')
    check = 0
    rand_num = random.randrange(1, 11)
    while check == 0:
        guess_num = int(input('Введите число от 1 до 10: '))
        if rand_num == guess_num:
            check += 1
            return print('Ура ты угадал!!!')


if __name__ == "__main__":
    name, age = input_data()
    rez_func(name, age)
    random_number()
