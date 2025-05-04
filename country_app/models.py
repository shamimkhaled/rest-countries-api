from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=4, unique=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    population = models.IntegerField()
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    timezones = models.JSONField()
    languages = models.JSONField()
    flag_png = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
        
        