from day_2.common import MyException


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(number):
        if type(number) == int:
            if number >= 0:
                return function(number)
            else:
                raise MyException
        else:
            raise MyException

    return wrapper


def cache_value(function):
    """
    Обертка, которая кэширует результат последних пяти вызовов.
    """
    dict_of_called = {}

    def wrapper(number):
        keys = dict_of_called.keys()

        if number in keys:
            pass
        elif len(dict_of_called) <= 5:
            dict_of_called[number] = function(number)
        else:
            dict_of_called.pop(keys[0])
            dict_of_called[number] = function(number)

        return dict_of_called[number]

    return wrapper
