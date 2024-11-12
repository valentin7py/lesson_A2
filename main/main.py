"""
Написать декоратор для функции main, в котором будет в бесконечном цикле вызов main до тех пор,
пока main функция не вернет значение True. True значение должно вернуться в том случае,
если в main не было ни одной ошибки авторизации и пользователь был успешно авторизовано/зарегистрирован
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

def decor(func):
    def wraper():
        while True:
            if func() == True:
                break
            
    return wraper

@decor        
def main() -> bool:
    """Основная функция"""
    authenticator = Authenticator()

    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    
    if authenticator.login:     
        try:
            authenticator.authorize(login,password) # авторизация
            authenticator.user_greeting() # финальное приветсвие
            guess_number_game()
            return True
            
        except AuthorizationError as e:
            print(e)
    else:
        
        try:
            authenticator.registrate(login,password)# регистрируем пользователя
            guess_number_game()
            return True
            
        except RegistrationError as e:
            print(e)

    

if __name__ == "__main__":
    main()

