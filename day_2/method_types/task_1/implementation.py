class Coffee:
    def __init__(self):
        pass

    @classmethod
    def init_cappuccino(cls, ml_cappuccino=0):
        coffee = cls()
        coffee.cappuccino = ml_cappuccino
        return coffee

    @classmethod
    def init_latte(cls, ml_latte=0):
        coffee = cls()
        coffee.latte = ml_latte
        return coffee

    @classmethod
    def init_glace(cls, ml_glace=0):
        coffee = cls()
        coffee.glace = ml_glace
        return coffee

