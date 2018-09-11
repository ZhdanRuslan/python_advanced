"""
URL shortener.

Supported schemes: http, https.
"""
from random import choice
from string import ascii_letters, digits
from urllib.parse import urlparse

from django.conf import settings
from django.core.cache import cache
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect


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
    """
    Функция генерирующая случайную строку состоящую из символов и цифр
    """
    
    return ''.join(choice(ascii_letters + digits) for x in range(5))


def index(request):
    """
    Главная страница (в данном случае просто возврат строки в информационных целях)
    request - WSGIRequest
    """

    return HttpResponse('<h1> Main page in index func with method {} </h1>'.format(request.method))


def shorten(request, url):
    """
    Реализация логики сокращения ссылок. Работаем только по http или https, в противном случае 
    редирект на главную.
    Кэш Django используется в качестве хранения соответствий сокращенных и не сокращенных ссылок 
    TODO: Сделал костыльно с mailto:email@host.com (еще не разобрался до конца)
    """
    # if request.scheme == 'http' or request.scheme == 'https':
    if str(url).startswith('http') or str(url).startswith('https'):
        # if str(url).startswith('mailto:'):
        #     return redirect('/')
        generated_key = random_key()
        cache.add(generated_key, {'url': url, 'count': 0})
        return HttpResponse('<a href="http://localhost:8000/{0}">{1}</a>'\
        .format(str(generated_key), str(url)))
    else:
        return redirect('/')


def redirect_view(request, key):
    """
    Достаем из кеша и редиректим
    """
    cached = cache.get(key, None)
    if cached:
        cached['count'] += 1
        cache.set(key, cached)
        return redirect(cached['url'])
    else:
        return redirect('/')

def urlstats(request, key):
    """
    Статистика переходов по ссылке
    """
    cached = cache.get(key)
    if cached:
        return HttpResponse('Ref {} переходили {} раз'.format(cached['url'], cached['count']))
    else:
        return HttpResponse('No ref')

urlpatterns = [
    url(r'^$', index),
    # http://localhost:8000/shorten/<url>    
    url(r'shorten/(.+)$', shorten),
    # http://localhost:8000/urlstats/<key>
    url(r'urlstats/([\w\d]+)$', urlstats),
    # http://localhost:8000/<key>
    url(r'([\w\d]+)', redirect_view),
]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)