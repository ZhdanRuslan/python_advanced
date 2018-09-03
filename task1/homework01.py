# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

def fib():
   
    a, b = 1, 1
    while True:
        yield a            
        a, b = b, a + b 


def flatten(seq):
    try:
        first, *rest = seq
    except TypeError:
        return [seq]
    except ValueError:
        return []
    return flatten(first) + flatten(rest)



class call_count():
	def __init__(self, function):
		self.function = function
		self._call_count = 0

	def __call__(self, *args, **kwargs):
		self._call_count += 1
		return self.function(*args, **kwargs)

	@property
	def call_count(self):
		return self._call_count