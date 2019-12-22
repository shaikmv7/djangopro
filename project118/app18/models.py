from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='employees/')

    def __str__(self):
        return self.idno
