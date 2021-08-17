from day_7.queryset_methods.models import (
    OrderItem,
    Product
)


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    products = Product.objects.all()

    result = []
    for product in products:
        orderitem = OrderItem.objects.filter(product=product, order__date_formation__gte=begin,
                                             order__date_formation__lt=end)
        total_count = 0
        for item in orderitem:
            total_count += item.count
        if total_count == 0:
            continue
        else:
            result.append((product.name, int(total_count)))

    result = sorted(result, key=lambda x: x[0][1], reverse=True)
    if result:
        return list(filter(lambda x: x[1] == result[0][1], result))
    else:
        return result
