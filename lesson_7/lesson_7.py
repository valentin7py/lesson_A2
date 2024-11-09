"""/lesson7#readme

1.+ int(age) нужно сделать после очистки строки
от пробелов в конструкторе класса

2. в экземпляре класса создает переменную data_history,
которая является пустым списком,
но будет хранить объекты класса Data —
это вам необходимо знать для того,
чтобы вы могли сделать type hint для этой переменной

3. Счетчик попыток оставить на месте как есть

4. Где вызывать ValueError
Valentin: не понял 4 задание."""

import random
from exceptions import ValidateError


class Data:
    """Ввод даных и их первичная обработка"""

    def __init__(self, name: str, age: str):
        self.age = age
        self.name = name
        self.clear_whitespaces()
        self._validate_age_num()
        self.age = int(age)

    def clear_whitespaces(self) -> None:
        """Удаляет пробелы"""
        self.age = self.age.strip()
        self.name = self.name.strip()

    def _validate_age_num(self) -> None:
        """Проверка age на числовое значение"""
        if self.age.isdigit() == False:
            raise ValidateError('возраст должен быть числом')


class Validate:
    """Валидация данных"""

    def __init__(self):
        self.data_history = []  # список данных [0] - name, [1] - age

    def validate(self, data: Data):
        """Добавляем и проверяем данные"""
        self.data_history.append(data.name)  # добавляем имя в список data_histiry
        self.data_history.append(data.age) # добавляем возраст в список data_histiry
        self._validate_chek_data_history() # проверяем список на пустоту
        self.validate_name()  # проверка имени
        self.validate_age()  # проверка возраста

    def _validate_chek_data_history(self) -> None:
        """Проверяем пустой ли список data_history"""
        if not self.data_history:
            raise ValueError('Спсиок пуст, сначала заполните его')

    def validate_name(self) -> None:
        """Проверка имени"""
        name = self.data_history[0]
        if name == False:
            raise ValidateError('пустое значиние')
        elif name.count(' ') > 1:
            raise ValidateError(
                "В имени между буквами допускается только 1 пробел.")
        elif name.replace(' ', '').isalpha() == False:
            raise ValidateError('должны быть только буквы')
        elif len(name) < 3:
            raise ValidateError(
                'В имени должно быть минимум 3 символа.')

    def validate_age(self) -> None:
        """Проверка возраста"""
        age = self.data_history[-1]
        if age <= 0:
            raise ValidateError(
                'возраст не можеть быть равен или меньше 0')
        elif age < 14:
            raise ValidateError('Минимальный возраст — 14 лет')
        elif age > 111:
            raise ValidateError('Ты кто?')

    def get_passport_advise(self) -> None:
        """Проверяет возраст и записывает совет если надо"""
        age = self.data_history[-1]
        name = self.data_history[0]
        self.result_text = ''  # Выводим строку если не пустая
        default_text = f'Привет,{name.title()}! Тебе {age} лет.'
        if 16 <= age <= 17:
            self.result_text = default_text + 'Нужно не забыть получить первый паспорт'
        elif 25 <= age <= 26:
            self.result_text = default_text + 'Не забудь заменить паспорт по достижению 25 лет.'
        elif 45 <= age <= 46:
            self.result_text = default_text + 'Не забудь заменить паспорт по достижению 45 лет.'


def guess_number_game() -> None:
    """Игра угадай число"""
    print('Давай поиграем!')
    check = 0  # флаг для цикла
    count = 0  # кол-во попыток угадать число
    rand_num = random.randrange(1, 6)
    while check == 0:
        count += 1
        print(f'Попытка номер - {count}')
        guess_num = int(input('Введите число от 1 до 5: '))
        if rand_num == guess_num:
            check += 1
            return print('Ура ты угадал!!!')


def main() -> None:
    """Основная функция"""
    count = 0  # кол-во попыток ввода данных
    while True:
        count += 1
        print(f'Попытка номер: {count}')
        name = input('Введите имя: ')
        age = input('Введите возраст: ')
        try:
            # 1.создаем обьект класса 'person' с данными 'name' и 'age'
            person = Data(name, age)
            # 2.создаем обьект 'valid'
            valid = Validate() 
            # 3.проверяем данные (2 и 3 пункт наверно надо обьеденить)
            valid.validate(person)
        except ValidateError as e:
            print(f'я поймал ошибку: - {e}')
        else:
            break

    valid.get_passport_advise()  # проверяем возраст на совет.
    if valid.result_text:  # печатаем приветствие и совет если надо.
        print(valid.result_text)

    guess_number_game()  # запускаем игру угадай число


if __name__ == "__main__":
    main()
