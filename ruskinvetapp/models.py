from django.db import models

# Create your models here.
class Communications(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()