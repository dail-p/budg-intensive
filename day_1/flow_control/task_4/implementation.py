import datetime as dt


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    if isinstance(some_date, dt.date):
        return some_date + dt.timedelta(days=1)
    else:
        raise NotImplementedError
