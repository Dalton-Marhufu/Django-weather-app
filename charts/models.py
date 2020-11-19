from django.db import models

class CityCharts(models.Model):
    name = models.CharField(max_length=25)
    min_temp = models.IntegerField()
    max_temp = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
