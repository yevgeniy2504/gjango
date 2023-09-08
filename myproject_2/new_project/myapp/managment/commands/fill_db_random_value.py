# Добавить в базу данных случайные данные

from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from faker import Faker
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Добавить в базу данных случайные данные'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        fake = Faker(['ru_RU'])
        count = options['count']
        for _ in range(count):
            client = Client(name=fake.name(), email=fake.email(), phone=fake.phone_number(), address=fake.address())
            client.save()
            product = Product(name=fake.word(), description=fake.text(), price=random.randint(100, 10000),
                              quantity=random.randint(1, 100))
            product.save()
            order = Order(client=client, product=product, total=product.price * product.quantity,
                          date=datetime.now() - timedelta(days=random.randint(0, 100)))
            order.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу'))
