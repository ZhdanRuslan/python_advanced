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
# print(a.bonus)
