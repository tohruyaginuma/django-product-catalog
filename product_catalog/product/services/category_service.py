from product.models import Category


def list_categories():
    return Category.objects.order_by('id')
