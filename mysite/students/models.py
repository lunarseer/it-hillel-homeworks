from django.db import models


# Create your models here.

class GenericModel(models.Model):

    def values(self):
        def valid(key):
            if not key in ["_state"]:
                return True
            return None

        return {k: v for k, v in self.__dict__.items() if valid(k)}

    class Meta:
        abstract = True

class GenericPerson(GenericModel):

    firstname = models.CharField(max_length=30, default='John')
    lastname = models.CharField(max_length=30, default='Doe')
    age = models.IntegerField(default=16)

    def __str__(self):
        return "{} {} ({})".format(self.firstname, self.lastname, self.id)

    def values(self):
        return GenericModel.values(self)

    class Meta:
        abstract = True


class Student(GenericPerson):
    pass


class Teacher(GenericPerson):
    dicsiplines = models.JSONField(default=list)


class Group(GenericModel):

    name = models.CharField(max_length=30, default='unnamed group')
    students = models.JSONField(default=list)
    teachers = models.JSONField(default=list)

    def __str__(self):
        return "{} '{}'".format(self.__class__.__name__, self.name)