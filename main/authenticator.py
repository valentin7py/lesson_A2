"""lesson 11

1. Доделать последнюю домашку

2. В файл сохранять теперь данные в формате json

3. Разобраться как сериализовать datetime в json (Гугл, а потом написать подробно в комменте почему именно так)"""
import os
from exceptions import RegistrationError, AuthorizationError
import datetime
import json

class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0  # количество проваленных попыток (ошибки)

        if self._is_auth_file_exist():  # проверяем есть создан ли файл
            self._read_auth_file()  # записываем данные из файла в переменные об.класса
        else:
            print('Регистрация')

    def _is_auth_file_exist(self) -> bool:
        """Проверяем наличие файла `auth.txt` рядом (в той же папке)"""
        is_file_exist = "/home/valenit/Документы/studies/lesson_a/lessons_A/main/auth.json"
        #  почему то рабоатет только с полным путем.
        if os.path.isfile(is_file_exist):
            return True
        return False

    def _read_auth_file(self) -> None:
        """Данные из файла записываем в переменные"""
        f = open('main/auth.json')
        dict_data = json.load(f)
        self.login = dict_data['login']
        self._password = dict_data['password']
        self.last_success_login_at = dict_data['last_success_login_at']
        self.errors_count = dict_data['errors_count']
        

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

    def registrate(self, login: str, password: str)-> None:
        """Проверяем зарегистрирован ли пользователь"""
        if self.login:  # проверка наличия файла в папке
            self.errors_count += 1
            raise RegistrationError(
                "Пользвоатель с таким именем уже существует")

        if login:
            self.login = login
            self._password = password
            self._update_auth_file()
        else:
            self.errors_count += 1
            self._update_auth_file
            raise RegistrationError("Ошибка: пустой логин")

    def _update_auth_file(self)-> None:
        """Перезаписывает данные в json файл"""
        utc_now = datetime.datetime.utcnow() # получаем время 
        utc_date_time = utc_now.strftime("%Y-%m-%d %H:%M:%S") # переводим в удобный формат
        data = {'login': self.login, 'password': self._password,
                'last_success_login_at':utc_date_time , 'errors_count': self.errors_count}
        with open('main/auth.json','w') as file:
            json.dump(data,file)
            
    def user_greeting(self) -> None:
        """Финальное привествие вынес в отдельную функцию"""
        print(
            f'Привет {self.login}\nВремя входа - {self.last_success_login_at}\nКол-во пыпоток входа - {self.errors_count}')
