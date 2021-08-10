import time


def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(number):
        start_time = time.time()
        base_result = function(number)
        print(f'{time.time() - start_time} second')

        return base_result

    return wrapper
