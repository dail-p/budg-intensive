from day_7.queryset_methods.models import Order


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    return Order.objects.select_related('customer').filter(customer_name=name).count()
