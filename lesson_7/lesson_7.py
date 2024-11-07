"""/lesson7#readme

1.+ int(age) нужно сделать после очистки строки
от пробелов в конструкторе класса

2. в экземпляре класса создает переменную data_history,
которая является пустым списком,
но будет хранить объекты класса Data —
это вам необходимо знать для того,
чтобы вы могли сделать type hint для этой переменной

3. Счетчик попыток оставить на месте как есть

4. Где вызывать ValueError"""

import random


class Data:
    def __init__(self, name: str, age: str):
        self.age = age
        self.name = name
        self.clear_whitespaces()
        self.age = int(age)
        

    def clear_whitespaces(self):
        self.age = self.age.strip()
        self.name = self.name.strip()


class Validate:
    def __init__(self):
        self.data_history = []
        
    def validate(self, data: Data):
        self.data_history.append(data.name)
        self.data_history.append(data.age)
        self.validate_name()
        self.validate_age()

    def validate_name(self):
        name = self.data_history[0]
        if name == False:
            raise Exception('Ошибка: пустое значиние')
        elif name.count(' ') > 1:
            raise Exception(
                "Ошибка: В имени между буквами допускается только 1 пробел.")
        elif name.replace(' ', '').isalpha() == False:
            raise Exception('Ошибка: должны быть только буквы')
        elif len(name) < 3:
            raise Exception(
                'Ошибка: В имени должно быть минимум 3 символа.')

    def validate_age(self):
        age = self.data_history[-1]
        if age <= 0:
            raise Exception(
                'Ошибка: возраст не можеть быть равен или меньше 0')
        elif age < 14:
            raise Exception('Ошибка: Минимальный возраст — 14 лет')
        elif age > 111:
            raise Exception('Ты кто?')

    def get_passport_advise(self):
        """Результирующая функция"""
        age = self.data_history[-1]
        name = self.data_history[0]
        self.result_text = ''
        default_text = f'Привет,{name.title()}! Тебе {age} лет.'
        if 16 <= age <= 17:
            self.result_text = default_text + 'Нужно не забыть получить первый паспорт'
        elif 25 <= age <= 26:
            self.result_text = default_text + 'Не забудь заменить паспорт по достижению 25 лет.'
        elif 45 <= age <= 46:
            self.result_text = default_text + 'Не забудь заменить паспорт по достижению 45 лет.'


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
        name = input('Введите имя: ')
        age = input('Введите возраст: ')
        try:
            person = Data(name, age)
            valid = Validate()
            valid.validate(person)
        except Exception as e:
            print(f'я поймал ошибку: - {e}')
        else:
            break

    
    valid.get_passport_advise()
    if valid.result_text:
         print(valid.result_text)


if __name__ == "__main__":
    main()

# def main() -> None:
#     count = 0
   
#     while True:
        
#         count += 1
#         print(f'Попытка номер: {count}')
#         name = clear_whitespaces(input('Введите имя: '))
#         age = clear_whitespaces(input('Введите возраст: '))

#         try:
#             age = int(age)
#         except ValueError:
#             print(f'я поймал ошибку: введите числовое значение')
#             continue

#         try:
#             validate_age(age)
#             validate_name(name)
#         except Exception as e:
#             print(f'я поймал ошибку: - {e} ')
#         else:
#             break
#     get_passport_advise(name,age)
#     if result_text:
#         print(result_text)
    
#     guess_number_game()
    

# if __name__ == "__main__":
#     main()
