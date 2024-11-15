"""
Хеширование паролей с pbkdf2_hmac
показался достаточно безопасным, так как для получения ключей использует псевдослучайную функцию.
"""
from dataclasses import dataclass
import re
import os
import hashlib
from exceptions import ValidateError
import json
import binascii
@dataclass
class Validate:
    """класс валидации пароля и логина"""
    email: str | None = None
    password: str | None = None
    dict_hash: dict | None = None

    def _valid_forma_password(self,password) -> None:
        """проверяем пароль на несколько условий"""
        result = re.match(
            r'(?=.*\W)(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,}',password)
        if result is None:
            raise ValidateError(
                f'Ошибка: пароль должен иметь\n-минимум 4 символа\n-минимум один заглавный символ\n-минимум один прописной символ\n-минимум одна цифра\n-минимум один спецсимвол.  ')
        

    def _valid_forma_email(self,email) -> None:
        """проверяем логин на несколько условий"""
        result = re.match(
            r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', email)
        if result is None:
            raise ValidateError(
                f'Ошибка: логин должен выгляедть примерно так ---> name@mail.com ')
        
        
    def _hash_password(self,password) -> None:
        """хеш функция пароля при регистрации.
           1.получаем хеш пароля
           2.перводим в формат Hex
           3.довавляем в словаррь
           4.создаем json файл с хешами(в формате Hex)"""
        salt = os.urandom(32)  # соль. используеться для шифрования пароля .
        key = hashlib.pbkdf2_hmac(
            'sha256',  # алгоритм хеширования
            password.encode('utf-8'),  # Ковекртируем пароль в байты
            salt,# "соль"(рандомный код) вроде  добавляется к началу хеша пароля чем  усложняет взлом пароля через "грубую чису(перебором)"
            1000  # Рекомендуется использовать хотя бы 100000 итераций SHA-256
        )
        hex_key = binascii.hexlify(key).decode('utf-8') # переобразовываем  в Hex так как json не поддверживает байты
        hex_salt = binascii.hexlify(salt).decode('utf-8')
        dict_hash = { # словарь с солью и хешем для удобного записи в json
            'key': hex_key,
            'salt': hex_salt
        }
        
        with open('main/data_hash.json', 'w') as f:
            json.dump(dict_hash, f) # записываем данные в формате Hex в json
        

    
    def valid_password(self, password_new: str) -> bool:
        """проверка пароля при авторизации
           1. получаем основной пароль из data_hash.json
           2. переводим его из Hex обратно в байты
           3. с помощью старой соли создаем новый хеш
           4. сравниваем результат"""
        with open('main/data_hash.json', 'r') as f:
            data_hash = json.load(f)  # получаем данные в Hex 
        salt_old = binascii.unhexlify(data_hash['salt'])  # переобразовываем в обртано в байты, нужна старая соль для генерации хеша
        key_old = binascii.unhexlify(data_hash['key']) # переобразовываем в обртано в байты
        key_new = hashlib.pbkdf2_hmac(
            'sha256',  # алгоритм хеширования
            password_new.encode('utf-8'),# Ковекртируем пароль в байты
            salt_old, #  используем соль из из своего пароля
            1000)  # Рекомендуется использовать хотя бы 100000 итераций SHA-256
        print(f'old_key - {key_old}\nkey_new - {key_new}')
        if key_new != key_old: #  сравниваем байтовые значения хешей
            raise ValidateError('Ошибка: хеши не сходятся')



    
