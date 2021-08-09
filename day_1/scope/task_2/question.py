"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))



"""
Будет выведена строка "Test message", а поcле None. При выполнении функции data_transmitter интерпретатор не нашел в 
локальной области видимости переменную message, но нашел ее на уровень выше в функции transmit_to_space. Также в функции 
transmit_to_space не встречаются операторы return, поэтому она возвращает None.
"""