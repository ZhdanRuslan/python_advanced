"""
URL shortener.

Supported schemes: http, https.
"""

from django.conf import settings
from django.core.cache import cache
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect

from random import choice
from string import ascii_letters, digits
from urllib.parse import urlparse

# Задание 2. URL shortener
#
# Реализуйте сервис для сокращения ссылок. Примеры таких сервисов:
# http://bit.ly, http://t.co, http://goo.gl
# Пример ссылки: http://bit.ly/1qJYR0y
#
# Вам понадобится реализовать функции
#  - для генерации ключа
#  - для обработки запроса для сабмита URL
#  - для редиректа с короткого URL на исходный.
#
# Для хранения соответствий наших коротких ключей и полных URL
# мы будем использовать кеш Django, django.core.cache
# Экземпляр cache уже импортирован, и используется следующим образом.
# Сохранить значение:
#
#  cache.add(key, value)
#
# Извлечь значение:
#
#  cache.get(key, default_value)
#
# Второй, опциональный аргумент метода get - значение по умолчанию,
# если ключ не найден в кеше.
#
# Для проверки корректности реализации ваших функций,
# запустите тесты на выполнение:
#
# pytest test_homework02.py
#
# Также вы можете запустить сервер для разработки, и посмотреть
# ответы ваших функций в браузере:
#
# python homework02.py runserver


if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
    )


def random_key():
    return ''.join(choice(choice(ascii_letters) + choice(digits)) for i in range(50) if i % 2)


def index(request):  
    return HttpResponse('Main page in index func')


def shorten(request, url):
    
    if (request.scheme == 'http' or request.scheme == 'https'):
    # and not url.startwith('mailto:'):
        if url[0:6]=='mailto':
            return redirect('/')
        generated_key = random_key()
        cache.add(generated_key, url)
        return HttpResponse('<a href="http://localhost:8000/{0}">{1}</a>'\
        .format(generated_key, generated_key))
    else:
        return redirect('/')


def redirect_view(request, key):

    cached = cache.get(key, None)
    if cached == None:
        return redirect('/')
    else:
        return redirect(cached)

def urlstats(request, key):
    """
    (Опционально)

    Реализуйте счетчик кликов на сокращенные ссылки.
    В теле ответа функция должна возращать количество
    переходов по данному коду.
    """
    pass


urlpatterns = [
    url(r'^$', index),
    # http://localhost:8000/shorten/<url>    
    url(r'shorten/(.+)', shorten),
    # http://localhost:8000/<key>
    url(r'([\w\d]+)', redirect_view),
    # http://localhost:8000/urlstats/<key>    
    url(r'urlstats/([\w\d]+)', urlstats),
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
