from django.db import models


class Student(models.Model):

    class Grade(models.IntegerChoices):
        EXCELLENT = 5, 'Excelent'
        GOOD = 4, 'Good'
        SATISFACTORY = 3, 'Satisfactory'
        UNSUTISFACTORY = 2, 'Unsatisfactory'

    surname = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True)
    birthday = models.DateTimeField(blank=True, null=True, db_index=True)
    grade = models.SmallIntegerField(choices=Grade.choices,
                                     blank=True,
                                     null=True,
                                     db_index=True)
