from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)

class Transport(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    link = models.URLField()
    start = models.ForeignKey(City, related_name='start', on_delete=models.PROTECT)
    end = models.ForeignKey(City, on_delete=models.PROTECT)
