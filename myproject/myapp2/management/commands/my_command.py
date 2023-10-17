from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Prints "Hello world" to the console'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello world")
