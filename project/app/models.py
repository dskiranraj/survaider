from django.db import models


class Employee(models.Model):
    age = models.IntegerField()
    work = models.CharField(max_length=100)
    fnlwgt = models.IntegerField()
    education = models.CharField(max_length=100)
    education_num = models.IntegerField()
    martial_status = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100,null=True)
    relationship = models.CharField(max_length=100)
    race = models.CharField(max_length=100,null=True)
    sex = models.CharField(max_length=100,null=True)
    capital_gain = models.IntegerField()
    capital_loss = models.IntegerField()
    hours_per_week = models.IntegerField()
    native_country = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return self.work
