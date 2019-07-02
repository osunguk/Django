from django.db import models

# Create your models here.
class App(models.Model):
    inputData = models.CharField(max_length = 200)

    def __str__(self):
        return self.inputData