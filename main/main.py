"""
4. *Написать класс валидатора, написать валидацию для пароля:
минимум 4 символа, минимум один заглавный символ, минимум один прописной символ, 
минимум одна цифра, минимум один спецсимвол.
Хэшировать пароль любым алгоритмом на выбор, обосновать в комменте выбор алгоритма (можно хоть свой сделать). Написать метод валидации почты.
Вместо логина у вас должен быть ввод почтового адреса.
Valentin : при данной реализации в auth.json количетво попыток не увеличивается !!!
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
    

    try:
        validator._valid_forma_email(email) # проверяем пароль 
        validator._valid_forma_password(password)  
    except ValidateError as e:
        print(e)
        return False

    if authenticator.email:     
        try:
            validator.valid_password(password) # сравниваем хеш нового и старого пароля
            authenticator.authorize(email,password) # авторизация
            authenticator.user_greeting() # финальное приветсвие
            guess_number_game()
            return True
            # m@m.m  mM@1
        except (ValidateError,AuthorizationError) as e:
            print(e)
    else: 
        try:#
            validator._hash_password(password) # хэшируем пароль
            authenticator.registrate(email,password)# регистрируем пользователя
            guess_number_game()
            return True
            
        except (ValidateError,RegistrationError) as e:
            print(e)
   
    

if __name__ == "__main__":
    main()
    

