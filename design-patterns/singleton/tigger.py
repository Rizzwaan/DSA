# make trigger class private add _ to

class _Tigger:

    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return "Grrrr!"


# create a private module scoped varible called _instance and initialize it with None
_instance = None


# Same name as class with no variable
def Tigger():
    global _instance
    if _instance is None:
        _instance = _Tigger()
    return _instance
