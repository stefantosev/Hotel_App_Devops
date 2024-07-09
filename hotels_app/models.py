from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Employee(models.Model):
    WORK_CHOICES = [
        ('Receptioner', 'REC'),
        ('Manager', 'MAN'),
        ('Cleaner', 'CLE')
    ]

    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    year = models.IntegerField()
    type = models.CharField(max_length=100, choices=WORK_CHOICES)
    task_description = models.CharField(max_length=25)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True, limit_choices_to={'type': 'Cleaner'})  #za prazno da se ostavi null

    def __str__(self):
        return f"{self.name} - {self.last_name}"

class Room(models.Model):
    r_number = models.IntegerField()
    bed_number = models.IntegerField()
    have_Terasa = models.BooleanField()
    status_Cleaned = models.BooleanField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.r_number}"



class Reservation(models.Model):
    code = models.CharField(max_length=25)
    start = models.DateField()
    end = models.DateField()
    id_picture = models.ImageField(upload_to='images/')
    isReserved = models.BooleanField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} - {self.start}'
