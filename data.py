from random import randint

class Person:
    user_name = 'Александр'
    email = f'Baranov@yandex.ru'
    password = f'12345Qwe'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@vk.com'
    password = f'{randint(1000, 9999)}Qwe'