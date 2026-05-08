from product.models import Tag


def list_tags():
    return Tag.objects.all()
