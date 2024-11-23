"""
Valentin : не совсем понял как можно хешировать пароль не записывая соль в сторонии файлы или бд.
так как она всегда рандомная при запуске программы. пришлось использовать мастер соль и брать пароль из файла.
и не понял зачем хешировать пароль при регистрации.если мы всеравно не записываем хеш в сторонии файлы.
"""
from dataclasses import dataclass
import re
import os
import hashlib
from exceptions import ValidateError
import json

@dataclass
class Validate:
    """класс валидации пароля и логина"""
    compare_key : bytes | None = None
    key: bytes | None = None
    master_salt: bytes  = b'\x80\xd0ht\xb6]Qh\x17\xf0\xb1\x85\xbb\xf2\x99\xa38\x11\x9fed">(\xcaA\xa0Y\xb8\x83\xe5\xf4'
    
    def valid_email_pass(self,email,password):
        """проверка пароля ,почты
           хешируем пароли и сравниваем их"""
        self._valid_forma_email(email)
        self._valid_forma_password(password)
        self._hash_password(password)

    def _valid_forma_password(self, password) -> None:
        """проверяем пароль на несколько условий"""
        result = re.match(
            r'(?=.*\W)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,}', password)
        if result is None:
            raise ValidateError(
                f'Ошибка: пароль должен иметь\n-минимум 4 символа\n-минимум один заглавный символ\n-минимум один прописной символ\n-минимум одна цифра\n-минимум один спецсимвол.  ')

    def _valid_forma_email(self, email) -> None:
        """проверяем логин на несколько условий"""
        result = re.match(
            r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', email)
        if result is None:
            raise ValidateError(
                f'Ошибка: логин должен выгляедть примерно так ---> name@mail.com ')

        
    def _is_auth_file_exist(self) -> bool:
        """Проверяем наличие файла `auth.txt` рядом (в той же папке)"""
        is_file_exist = "main/auth.json"
        return os.path.isfile(is_file_exist)            

    def _hash_password(self, password) -> None:
        """функция хеширования паролей и сравнения их
           при авторизации создаем хеш пароля из файла и при попытке авторизации
           сравниваем сзначения 
           используем мастер соль так как нельзя записывать данные в файлы 
            ---> надо подумать как избежать дублирование кода """
        if self._is_auth_file_exist():
            f = open('main/auth.json')
            dict_data = json.load(f)
            orginal_password = dict_data['password'] # пароль из файла
            
            self.key = hashlib.pbkdf2_hmac(
                'sha256',  # алгоритм хеширования
                orginal_password.encode('utf-8'),  # Ковекртируем пароль в байты
                # "соль"(рандомный код) вроде  добавляется к началу хеша пароля чем  усложняет взлом пароля через "грубую чису(перебором)"
                self.master_salt,
                1000  # Рекомендуется использовать хотя бы 100000 итераций SHA-256
            )
            
            self.compare_key = hashlib.pbkdf2_hmac(
            'sha256',  # алгоритм хеширования
            password.encode('utf-8'),  # Ковекртируем пароль в байты
            # "соль"(рандомный код) вроде  добавляется к началу хеша пароля чем  усложняет взлом пароля через "грубую чису(перебором)"
            self.master_salt,
            1000  # Рекомендуется использовать хотя бы 100000 итераций SHA-256
            )
            
            print(f'old_key - {self.key}\nkey_new - {self.compare_key}')
            if self.key != self.compare_key:  # сравниваем байтовые значения хешей
                raise ValidateError('Ошибка: хеши не сходятся')
        

  
