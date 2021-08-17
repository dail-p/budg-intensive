from day_7.queryset_methods.models import (
    Customer,
)
from django.db.models import (
    Count,
    Min,
)


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    queryset = Customer.objects \
        .filter(order__date_formation__gte=begin, order__date_formation__lt=end) \
        .annotate(num_order=Count('order'), date=Min('order__date_formation')).order_by('num_order', ) \
        .values('name', 'num_order') \
        .order_by('-num_order', 'date', 'name')

    if queryset.exists():
        top_customer = queryset.first()
        return top_customer['name'], top_customer['num_order']
    else:
        return None
