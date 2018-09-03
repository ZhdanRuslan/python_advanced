class Money:
    def __init__(self, currency):
        self._currency = currency
        self._amount = None

    def __get__(self, obj, owner):
        return self._amount

    def __set__(self, obj, amount):
        obj._amount = amount

class Account:
    def __init__(self):
        self._primary = Money('UAH')
        self._bonus = Money('UAH')

a = Account()
a.primary = 100
print(a.primary)

# --------------------------------------------------------------
# str, list, dict, tuple, int, float
from collections import Sequence, Mapping
def encode(val):
    if isinstance(val, str):
        print('Got string')
    elif isinstance(val, Sequence):
        print('Got sequence')
    elif isinstance(val, Mapping):
        print('Got mapping')
    else:
        raise NotImplementedError
        
