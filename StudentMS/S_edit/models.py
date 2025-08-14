from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
