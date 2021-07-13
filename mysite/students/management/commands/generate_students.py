from random import randrange

from django.core.management.base import BaseCommand, CommandError
from students.models import Student

from faker import Faker


class Command(BaseCommand):
    help = 'Generate numbers of students'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100)

    def handle(self, **options):
        count = options.get('count', 0)
        if count:
            gen = Faker()
            students = []
            for _ in range(count):
                student = Student.objects.create(firstname=gen.first_name(),
                                              lastname=gen.last_name(),
                                              age=randrange(16, 50))
                students.append(student)
            responce = [x.values() for x in students]
        