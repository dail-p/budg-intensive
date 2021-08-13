
def fib(n):
    """
    Функция, которая возвращает n-ое число последовательности Фибоначчи
    """
    fib1, fib2 = 1, 1
    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
