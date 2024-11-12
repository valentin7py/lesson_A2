"""
lesson 9
"""
from authenticator import Authenticator
from exceptions import RegistrationError,AuthorizationError
import random

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
    authenticator = Authenticator()
    
    while True:
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        
        if authenticator.login:     
            try:
                authenticator.authorize(login,password) # авторизация
                authenticator.user_greeting() # финальное приветсвие
                break
            except AuthorizationError as e:
                print(e)
        else:
            
            try:
                authenticator.registrate(login,password)# регистрируем пользователя
            except RegistrationError as e:
                print(e)
            break

    guess_number_game()  # запускаем игру угадай число


if __name__ == "__main__":
    main()
