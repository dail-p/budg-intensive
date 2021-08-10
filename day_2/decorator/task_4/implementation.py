import time

from day_2.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def call_decorator(function):
        def wrapper():
            for iter in range(times):
                try:
                    base_result = function()
                except Exception:
                    time.sleep(delay)
                    continue
                else:
                    break
            else:
                raise MyException

            return base_result

        return wrapper

    return call_decorator

