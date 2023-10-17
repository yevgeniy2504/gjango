from django.core.management.base import BaseCommand
import models


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        user = models.User(name='John', email='qwerqdfdf@mail.ru', password='123456', age=25)
        ...
        user.save()
        self.stdout.write(f'Successfully created new user {user}')
