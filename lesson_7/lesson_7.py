# exception
"""

1. оптимизировать алгоритм
+2.  переименовать функции:
  +  1. 'validate_name' - проверка имени
  +  2. 'validate_age' - проверка возраста
  +  3.'clear_whitespaces' - функция очистки строки от пробелов в начале и конце
  +  4. 'get_passport_advise' - функция получению совета паспорта
  +  5. 'guess_number_game' -  игра ,генерирует число от 1 до 5 .пользователь должен отгадать.
3. все функции валидации "validate_name" и 'validate_age' должны возращать None ,
   если ошибка делать raise Exception (текс ошибки)
4. Использовать функию 'clear_whitespaces' так же для строки в которой должно быть число.
5. В  функции 'main' , необходимо отловить ошибки из функций 'validate_name' и 'validate_age'.
   вывести пользователю: "я поймал ошибку: {текс ошибки}". и елси была ошибка заново запросить данные у пользователя.
6. В  функции 'main' , обрабатывать ошибку valueError (не используем Exception) во время перевода строки к int.
7. перед запроса данных в main надо указывать счетчик ввода начиная с первой попытки.
8. во время игры угадай число тоже должен быть счетчик, отоброжать с какой попытки угадал. начиная с 1.


"""
import random


def clear_whitespaces(name: str) -> str:
    """Удаляет пробелы. """
    return name.strip()


def validate_name(name: str) -> None:
    """Проверкака имени"""
    if name == False:
        raise Exception('sdssadsa')
    elif name.count(' ') > 1:
        raise Exception(
            "Ошибка: В имени между буквами допускается только 1 пробел.")
    elif name.isalpha() == False:
        raise Exception('Ошибка: должны быть только буквы')
    elif len(name) < 3:
        raise Exception('Ошибка: В имени должно быть минимум 3 символа.')


def validate_age(age: int) -> None:
    if age <= 0:
        raise Exception('Ошибка: возраст не можеть быть равен или меньше 0')
    elif age < 14:
        raise Exception('Ошибка: Минимальный возраст — 14 лет')
    elif age > 111:
        raise Exception('Ты кто?')


def get_passport_advise(name: str, age: int) -> str:
    """Результирующая функция"""
    default_text = f'Привет,{name.title()}! Тебе {age} лет.'
    if 16 <= age <= 17:
        return default_text + 'Нужно не забыть получить первый паспорт'
    elif 25 <= age <= 26:
        return default_text + 'Не забудь заменить паспорт по достижению 25 лет.'
    elif 45 <= age <= 46:
        return default_text + 'Не забудь заменить паспорт по достижению 45 лет.'


def guess_number_game() -> None:
    print('Давай поиграем!')
    check = 0
    count = 0
    rand_num = random.randrange(1, 6)
    while check == 0:
        count += 1
        print(f'Попытка номер - {count}')
        guess_num = int(input('Введите число от 1 до 5: '))
        if rand_num == guess_num:
            check += 1
            return print('Ура ты угадал!!!')


def main() -> None:
    count = 0
    while True:
        count += 1
        print(f'Попытка номер: {count}')
        name = clear_whitespaces(input('Введите имя: '))
        age = clear_whitespaces(input('Введите возраст: '))

        try:
            age = int(age)
        except ValueError as e:
            print(f'я поймал ошибку: - {e}')

        try:
            validate_age(age)
            validate_name(name)
        except Exception as e:
            print(f'я поймал ошибку: - {e} ')
        else:
            break

    if age in [16, 17, 25, 26, 45, 46]:
        print(get_passport_advise(name, age))

    guess_number_game()


if __name__ == "__main__":
    main()
