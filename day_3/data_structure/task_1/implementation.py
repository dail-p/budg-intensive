class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """

    def __init__(self, *args):
        self._tuple = args

    def __getitem__(self, key):
        return self._tuple[key]

    def __str__(self):
        return str(self._tuple)

    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        count = 0
        for item in self._tuple:
            if item == value:
                count += 1

        return count

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        for count, item in enumerate(self._tuple):
            if item == value:
                return count
        else:
            raise ValueError


a = Tuple(1, 2, 3)
print(a)
