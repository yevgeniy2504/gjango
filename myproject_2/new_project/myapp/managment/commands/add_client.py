# Добавить клиента в базу

from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Добавить клиента в базу'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        client = Client(name=options['name'], email=options['email'], phone=options['phone'], address=options['address'])
        client.save()
        self.stdout.write(self.style.SUCCESS('Клиент успешно добавлен в базу'))





