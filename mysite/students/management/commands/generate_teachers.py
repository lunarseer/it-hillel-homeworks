from random import randrange

from django.core.management.base import BaseCommand, CommandError
from students.models import Teacher

from faker import Faker


class Command(BaseCommand):
    help = 'Generate numbers of teachers'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100)

    def handle(self, **options):
        count = options.get('count', 0)
        if count:
            gen = Faker()
            teachers = []
            for _ in range(count):
                teacher = Teacher.objects.create(firstname=gen.first_name(),
                                              lastname=gen.last_name(),
                                              age=randrange(16, 70))
                teachers.append(teacher)
            responce = [x.values() for x in teachers]
        