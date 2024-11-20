from django.db import models


class Todoitems(models.Model):
    Title=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title