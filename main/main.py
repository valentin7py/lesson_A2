"""
Alexandr:
5.вызывать протектед метод вне класса — не ок
6.очень странно, что "класс валидации пароля и логина" по какой-то причине записывает что-то в файл.
хотя класс и методы должны отвечать только за решение одной конкретной проблемы. Тоже самое касается valid_password
"""
from authenticator import Authenticator
from validator import Validate
from exceptions import RegistrationError,AuthorizationError,ValidateError
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
authenticator = Authenticator()
validator = Validate()
@decor        
def main() -> bool:
    """Основная функция"""
    email = input('Введите логин: ')
    password = input('Введите пароль: ')
    

    if authenticator.email:     
        try:
            validator.valid_email_pass(email,password)
            authenticator.authorize(email,password) # авторизация
            authenticator.user_greeting() # финальное приветсвие
            guess_number_game()
            return True
            # m@m.m  mM@1
        except (ValidateError,AuthorizationError) as e:
            print(e)
    else: 
        try:#
            validator.valid_email_pass(email,password)
            authenticator.registrate(email,password)# регистрируем пользователя
            guess_number_game()
            return True
            
        except (ValidateError,RegistrationError) as e:
            print(e)
   
    

if __name__ == "__main__":
    main()
    

#MmDSSA2D@MMM.MMASD 
# "2024-11-22 13:51:10"