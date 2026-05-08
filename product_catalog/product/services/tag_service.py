from product.models import Tag


def list_tags():
    return Tag.objects.order_by('id')
