from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    description=models.TextField()
    star=models.IntegerField()

    def __str__(self):
        return self.name
