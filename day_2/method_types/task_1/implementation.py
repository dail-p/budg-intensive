class Coffee:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def init_cappuccino(cls, ml_cappuccino=0):
        coffee = cls(cappuccino=ml_cappuccino)
        return coffee

    @classmethod
    def init_latte(cls, ml_latte=0):
        coffee = cls(latte=ml_latte)
        return coffee

    @classmethod
    def init_glace(cls, ml_glace=0):
        coffee = cls(glace=ml_glace)
        return coffee
