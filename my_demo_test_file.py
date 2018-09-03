from random import choice
from string import ascii_letters, digits

# # print(''.join(choice(ascii_uppercase or digits) for i in range(12)))
# # s = ''.join(choice(ascii_letters) for i in range(50))
# s = ''.join(choice(choice(ascii_letters) + choice(digits)) for i in range(50) if i % 2)
# print(s)

def get_key():
    return ''.join(choice(choice(ascii_letters) + choice(digits)) for i in range(50) if i % 2)

from urllib.parse import urlparse

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
google = urlparse('https://www.google.com.ua/search?hl=ru&source=hp&ei=Dx-NW8WZJMeNsgHAkoFo&q=python+\
official+site&oq=python+off&gs_l=psy-ab.3.0.0l10.1931.7068.0.8850.12.11.0.0.0.0.111.999.5j5.11.0..3..0\
...1.1.64.psy-ab..1.10.998.0..0i131k1.90.6IUYpTGC9bw')

print(google.scheme)
res_map = {}



if google.scheme == 'http' or google.scheme == 'https':
    res_map[get_key()] = google.path

print(res_map)