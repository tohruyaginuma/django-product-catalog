# catalog/management/commands/seed.py
from django.core.management.base import BaseCommand
from product.models import Category, Tag, Product, ProductTag


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Categories
        category_names = [
            'Electronics', 'Clothing', 'Books', 'Food', 'Sports'
        ]
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name)
            categories.append(category)
            self.stdout.write(f'  [Category] {name} {"created" if created else "already exists"}')

        # Tags
        tag_names = [
            'Sale', 'New', 'Popular', 'Limited', 'Eco',
            'Premium', 'Imported', 'Local', 'Handmade', 'Organic'
        ]
        tags = []
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
            self.stdout.write(f'  [Tag] {name} {"created" if created else "already exists"}')

        # Products
        products_data = [
            {'name': 'Laptop Pro', 'description': 'High performance laptop for professionals', 'category': categories[0], 'tags': [tags[0], tags[5]]},
            {'name': 'Wireless Earbuds', 'description': 'Noise cancelling wireless earbuds', 'category': categories[0], 'tags': [tags[1], tags[2]]},
            {'name': 'Smartphone X', 'description': 'Latest smartphone with advanced camera', 'category': categories[0], 'tags': [tags[1], tags[3]]},
            {'name': 'Smart Watch', 'description': 'Fitness tracking smart watch', 'category': categories[0], 'tags': [tags[2], tags[5]]},
            {'name': 'Running Shoes', 'description': 'Lightweight shoes for marathon runners', 'category': categories[4], 'tags': [tags[0], tags[2]]},
            {'name': 'Yoga Mat', 'description': 'Eco friendly non-slip yoga mat', 'category': categories[4], 'tags': [tags[4], tags[7]]},
            {'name': 'Python Cookbook', 'description': 'Advanced recipes for Python developers', 'category': categories[2], 'tags': [tags[2], tags[6]]},
            {'name': 'Django for Beginners', 'description': 'Step by step guide to Django web framework', 'category': categories[2], 'tags': [tags[1], tags[2]]},
            {'name': 'Clean Code', 'description': 'A handbook of agile software craftsmanship', 'category': categories[2], 'tags': [tags[5], tags[2]]},
            {'name': 'Design Patterns', 'description': 'Elements of reusable object oriented software', 'category': categories[2], 'tags': [tags[5]]},
            {'name': 'Winter Jacket', 'description': 'Warm and waterproof jacket for cold weather', 'category': categories[1], 'tags': [tags[0], tags[6]]},
            {'name': 'Cotton T-Shirt', 'description': 'Comfortable everyday cotton t-shirt', 'category': categories[1], 'tags': [tags[7], tags[8]]},
            {'name': 'Denim Jeans', 'description': 'Classic slim fit denim jeans', 'category': categories[1], 'tags': [tags[2], tags[6]]},
            {'name': 'Wool Sweater', 'description': 'Handmade wool sweater for winter', 'category': categories[1], 'tags': [tags[8], tags[4]]},
            {'name': 'Organic Coffee', 'description': 'Single origin organic arabica coffee beans', 'category': categories[3], 'tags': [tags[9], tags[4]]},
            {'name': 'Green Tea', 'description': 'Premium Japanese matcha green tea', 'category': categories[3], 'tags': [tags[5], tags[9]]},
            {'name': 'Protein Bar', 'description': 'High protein snack bar for athletes', 'category': categories[3], 'tags': [tags[2], tags[1]]},
            {'name': 'Olive Oil', 'description': 'Extra virgin cold pressed olive oil', 'category': categories[3], 'tags': [tags[9], tags[6]]},
            {'name': 'Tennis Racket', 'description': 'Professional grade carbon fiber tennis racket', 'category': categories[4], 'tags': [tags[5], tags[3]]},
            {'name': 'Camping Tent', 'description': 'Lightweight 2 person camping tent', 'category': categories[4], 'tags': [tags[1], tags[4]]},
        ]

        for data in products_data:
            product, created = Product.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'category': data['category'],
                }
            )
            if created:
                for tag in data['tags']:
                    ProductTag.objects.get_or_create(product=product, tag=tag)
            self.stdout.write(f'  [Product] {product.name} {"created" if created else "already exists"}')

        self.stdout.write(self.style.SUCCESS('\nSeeding complete!'))
        self.stdout.write(f'  Categories : {Category.objects.count()}')
        self.stdout.write(f'  Tags       : {Tag.objects.count()}')
        self.stdout.write(f'  Products   : {Product.objects.count()}')