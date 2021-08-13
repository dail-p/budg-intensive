import time


def return_errors(filename):
    """
    Функция, которая возвращает строки из лога со словом error
    """
    subline = 'error'
    with open(filename, 'r') as f:
        generator = (line for line in f if subline in line or subline.upper() in line)
        return list(generator)


result = return_errors('log.txt')

