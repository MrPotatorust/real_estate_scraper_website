from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TableInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)


class ScrapedData(models.Model):

    table = models.ForeignKey(TableInfo, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    price_per_sqm = models.FloatField(null=True)
    area = models.FloatField(null=True)
    location = models.CharField(max_length=100)
    type_of_property = models.CharField(max_length=30)
    

class AnalysedData(models.Model):
    table = models.ForeignKey(TableInfo, on_delete=models.CASCADE)


    avg_price = models.FloatField(null=True)
    avg_price_per_sqm = models.FloatField(null=True)
    avg_sq_meter = models.FloatField(null=True)

    min_price = models.FloatField(null=True)
    min_price_per_sqm = models.FloatField(null=True)
    min_sq_meter = models.FloatField(null=True)

    max_price = models.FloatField(null=True)
    max_price_per_sqm = models.FloatField(null=True)
    max_sq_meter = models.FloatField(null=True)

    median_price = models.FloatField(null=True)
    median_price_per_sqm = models.FloatField(null=True)
    median_sq_meter = models.FloatField(null=True)
