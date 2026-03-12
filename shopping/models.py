from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
