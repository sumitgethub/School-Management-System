from django.db import models

class Gender(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(unique=True,max_length=50)

    def __str__(self):
        return self.value