def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    days = 0
    if month == 'январь':
        days = 31
    elif month == 'февраль':
        days = 28
    elif month == 'март':
        days = 31
    elif month == 'апрель':
        days = 30
    elif month == 'май':
        days = 31
    elif month == 'июнь':
        days = 30
    elif month == 'июль':
        days = 31
    elif month == 'август':
        days = 31
    elif month == 'сентябрь':
        days = 30
    elif month == 'октябрь':
        days = 31
    elif month == 'ноябрь':
        days = 30
    elif month == 'декабрь':
        days = 31
    else:
        days = 0

    return days

