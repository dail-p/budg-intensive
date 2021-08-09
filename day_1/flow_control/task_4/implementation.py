import datetime as dt


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    kwargs = {'year': some_date.year, 'month': some_date.month, 'day': some_date.day}
    long_months = (1, 3, 5, 7, 8, 10, 12)
    short_months = (4, 6, 9, 11)
    february = 2

    if some_date.month in long_months:
        if some_date.day == 31:
            if some_date.month == long_months[6]:
                kwargs['year'] += 1
            kwargs['month'] = 1
            kwargs['day'] = 1
        else:
            kwargs['day'] += 1

    elif some_date.month in short_months:
        if some_date.day == 30:
            kwargs['month'] += 1
            kwargs['day'] = 1
        else:
            kwargs['day'] += 1

    elif some_date.month == february:
        if some_date.day == 29:
            kwargs['month'] += 1
            kwargs['day'] = 1
        else:
            kwargs['day'] += 1

    else:
        raise NotImplementedError

    return some_date.replace(**kwargs)
