from random import randint

random_integer = randint(111, 999) # Генератор случайных чисел для логина
random_password = randint(100000, 999999) # Генератор случайных чисел для пароля

class Constants:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    NAME = 'dmitry_shiyanov'
    DEF_MAIL = 'dmitry_shiyanov_20_987@yandex.ru'
    DEF_PASSWORD = '123456'
    RANDOM_PASS = random_password
    RANDOM_MAIL = f'dmitry_shiyanov_20_{random_integer}@yandex.ru'