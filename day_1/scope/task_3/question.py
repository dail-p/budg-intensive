"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

"""
Будет выведено "3 3", так как оператор nonlocal позволяет изменять нелокальную переменную. 
"""