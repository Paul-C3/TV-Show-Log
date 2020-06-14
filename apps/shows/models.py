from django.db import models

class TVshows(models.Model):
    title = models.CharField(max_length=100)
    # network = models.CharField(max_length=100)
    # date = models.DateTimeField('date created')
    # description = models.TextField()
# Create your models here.
