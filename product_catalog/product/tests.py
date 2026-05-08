from django.test import TestCase

from product.models import Category, Tag, Product
from product.services.product_query_service import list_products


class ListProductsTest(TestCase):
    def setUp(self):
        self.category_a = Category.objects.create(name='Electronics')
        self.category_b = Category.objects.create(name='Books')

        self.tag_sale = Tag.objects.create(name='Sale')
        self.tag_new = Tag.objects.create(name='New')

        self.product_a = Product.objects.create(
            name='Laptop',
            description='High performance laptop',
            category=self.category_a,
        )
        self.product_a.tags.set([self.tag_sale])

        self.product_b = Product.objects.create(
            name='Python Cookbook',
            description='Advanced recipes for Python developers',
            category=self.category_b,
        )
        self.product_b.tags.set([self.tag_new])

        self.product_c = Product.objects.create(
            name='Smartphone',
            description='Latest smartphone',
            category=self.category_a,
        )
        self.product_c.tags.set([self.tag_sale, self.tag_new])

    def test_no_filters_returns_all(self):
        result = list_products()
        self.assertEqual(result.count(), 3)

    def test_filter_by_description(self):
        result = list_products(description='laptop')
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first(), self.product_a)

    def test_filter_by_description_case_insensitive(self):
        result = list_products(description='LAPTOP')
        self.assertEqual(result.count(), 1)

    def test_filter_by_category_ids(self):
        result = list_products(category_ids=[self.category_a.id])
        self.assertEqual(result.count(), 2)

    def test_filter_by_multiple_category_ids(self):
        result = list_products(category_ids=[self.category_a.id, self.category_b.id])
        self.assertEqual(result.count(), 3)

    def test_filter_by_tag_ids(self):
        result = list_products(tag_ids=[self.tag_sale.id])
        self.assertEqual(result.count(), 2)

    def test_filter_by_multiple_tag_ids_is_or(self):
        result = list_products(tag_ids=[self.tag_sale.id, self.tag_new.id])
        self.assertEqual(result.count(), 3)

    def test_combine_description_and_category(self):
        result = list_products(description='python', category_ids=[self.category_b.id])
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first(), self.product_b)

    def test_combine_description_and_tag(self):
        result = list_products(description='smartphone', tag_ids=[self.tag_sale.id])
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first(), self.product_c)

    def test_combine_description_category_and_tag(self):
        result = list_products(
            description='laptop',
            category_ids=[self.category_a.id],
            tag_ids=[self.tag_sale.id],
        )
        self.assertEqual(result.count(), 1)
        self.assertEqual(result.first(), self.product_a)

    def test_no_match_returns_empty(self):
        result = list_products(description='nonexistent')
        self.assertEqual(result.count(), 0)
