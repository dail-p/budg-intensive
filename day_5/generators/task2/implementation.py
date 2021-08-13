import time


def return_errors(filename):
    """
    Функция, которая возвращает строки из лога со словом error
    """
    f = open(filename, 'r')
    subline = 'error'
    for line in f:
        if subline in line or subline.upper() in line:
            yield line


result = return_errors('log.txt')
