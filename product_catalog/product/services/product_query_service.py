from product.models import Product


def list_products(description=None, category_ids=None, tag_ids=None):
    qs = Product.objects.select_related('category').prefetch_related('tags')

    if description:
        qs = qs.filter(description__icontains=description)

    if category_ids:
        qs = qs.filter(category_id__in=category_ids)

    if tag_ids:
        qs = qs.filter(tags__id__in=tag_ids)

    return qs.distinct()
