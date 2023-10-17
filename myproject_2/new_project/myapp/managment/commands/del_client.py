# Удаление клиента из базы данных

from django.core.management.base import BaseCommand, CommandError
from myapp.models import Client


class Command(BaseCommand):
    help = 'Удалить клиента из базы'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        try:
            client = Client.objects.get(name=options['name'])
            client.delete()
            self.stdout.write(self.style.SUCCESS('Клиент успешно удален из базы'))
        except Client.DoesNotExist:
            raise CommandError('Клиент с именем "%s" не существует' % options['name'])