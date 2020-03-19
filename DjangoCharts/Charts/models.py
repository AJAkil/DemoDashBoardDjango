from django.db import models


# Create your models here.
class DiseaseEntry(models.Model):
    country_name = models.CharField(max_length=300)
    number_effected = models.IntegerField()
    numbers_recovered = models.IntegerField()
    lat_long = models.CharField(max_length=500)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.country_name,self.number_effected,self.numbers_recovered,self.lat_long)