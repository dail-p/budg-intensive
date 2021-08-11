from day_2.common import MyException


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(number):
        if isinstance(number, int):
            if number >= 0:
                return function(number)
            else:
                raise MyException
        else:
            raise MyException

    return wrapper


def cache_value(function):
    """
    Обертка, которая кэширует результат предыдущих вызовов.
    """
    dict_of_called = {}

    def wrapper(number):
        if number not in dict_of_called:
            dict_of_called[number] = function(number)

        return dict_of_called[number]

    return wrapper



