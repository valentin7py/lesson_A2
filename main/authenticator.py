import os
from exceptions import RegistrationError, AuthorizationError
import datetime


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0  # количество проваленных попыток (ошибки)

        if self._is_auth_file_exist(): # проверяем есть создан ли файл
            self._read_auth_file() # записываем данные из файла в переменные об.класса
        else:
            print('Регистрация') 

    def _is_auth_file_exist(self) -> bool:
        """Проверяем наличие файла `auth.txt` рядом (в той же папке)"""
        is_file_exist = "/home/valenit/Документы/studies/lesson_a/lessons_A/main/auth.txt" 
        #  почему то рабоатет только с полным путем.
        if os.path.isfile(is_file_exist):
            return True
        return False

    def _read_auth_file(self):
        """Данные из файла записываем в переменные"""
        with open("main/auth.txt", 'r') as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = f.readline().strip()
            self.errors_count = int(f.readline().strip())

    def authorize(self, login: str, password: str) -> None:
        """1.Проеврка сущесвует ли  login.
           2.Сравниваем логин и пароль из файла и атрибута"""
        if login:
            if login != self.login or password != self._password:
                self.errors_count += 1
                self._update_auth_file()
                raise AuthorizationError('Неверный пароль или логин')
            else:
                self._update_auth_file()
        else:
            self.errors_count += 1
            raise AuthorizationError('Пустой логин')
            

    def registrate(self, login: str, password: str):
        """Проверяем зарегистрирован ли пользователь"""
        if self.login:  # проверка наличия файла в папке
            self.errors_count += 1
            raise RegistrationError("Пользвоатель с таким именем уже существует")

        if login: 
            self.login = login
            self._password = password
            self._update_auth_file()
        else:
            self.errors_count += 1
            self._update_auth_file
            raise RegistrationError("Ошибка: пустой логин")

    def _update_auth_file(self):
        """Перезаписывает данные в файл"""
        utc_now = datetime.datetime.utcnow()
        utc_date_time = utc_now.strftime("%m/%d/%Y, %H:%M:%S")
        self.last_success_login_at = utc_date_time
        with open('main/auth.txt', 'w') as f:
            f.write(f'{self.login}\n')
            f.write(f'{self._password}\n')
            f.write(f'{self.last_success_login_at}\n')
            f.write(f'{self.errors_count}')
    
    
    def user_greeting(self):
        """Финальное привествие вынес в отдельную функцию"""
        print(f'Привет {self.login}\nВремя входа - {self.last_success_login_at}\nКол-во пыпоток входа - {self.errors_count}')
          
        
           

   
    



