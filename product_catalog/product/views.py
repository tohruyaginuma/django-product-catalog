import logging

from django.http import HttpResponseBadRequest
from django.views.generic import TemplateView

from product.services.category_service import list_categories
from product.services.product_query_service import list_products
from product.services.tag_service import list_tags

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'product/index.html'

    def get(self, request, *args, **kwargs):
        description = request.GET.get('description', '')
        category_ids = request.GET.getlist('category_ids')
        tag_ids = request.GET.getlist('tag_ids')

        try:
            category_ids = [int(i) for i in category_ids]
        except ValueError:
            logger.warning('Invalid category_ids: %s', category_ids)
            return HttpResponseBadRequest('Invalid category_ids')

        try:
            tag_ids = [int(i) for i in tag_ids]
        except ValueError:
            logger.warning('Invalid tag_ids: %s', tag_ids)
            return HttpResponseBadRequest('Invalid tag_ids')

        logger.info(
            'list products description=%s category_ids=%s tag_ids=%s',
            description,
            category_ids,
            tag_ids,
        )

        products, product_count = list_products(
            description=description,
            category_ids=category_ids,
            tag_ids=tag_ids,
        )
        categories = list_categories()
        tags = list_tags()

        context = {
            'products': products,
            'product_count': product_count,
            'categories': categories,
            'tags': tags,
            'selected_category_ids': category_ids,
            'selected_tag_ids': tag_ids,
            'description': description,
        }
        return self.render_to_response(context)
