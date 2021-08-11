class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *args):
        if args is not None:
            self._tuple = [x for x in args]
        else:
            self._tuple = []

    def __getitem__(self, key):
        return self._tuple[key]

    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        count = 0
        for it in self._tuple:
            if it == value:
                count += 1

        return count

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        index = 0
        if value in self._tuple:
            for it in self._tuple:
                if it == value:
                    break
                index += 1

            return index

        else:
            raise ValueError
