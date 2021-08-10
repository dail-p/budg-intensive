from day_2.common import MyException


class ClassFather:
    registered_list = set()

    def __init__(self):
        pass

    def register(self):
        if type(self) != ClassFather:
            self.registered_list.add(type(self))
        else:
            raise MyException

    def get_name(self):
        if type(self) in self.registered_list:
            return self._name
        else:
            raise MyException


class User1(ClassFather):
    _name = 'first'


class User2(ClassFather):
    _name = 'second'

