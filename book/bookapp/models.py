from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)#obtaining the name fro author class onto this field
    price=models.IntegerField()
    publication_date=models.DateField(null=True, blank=True)   #if this field is empty no issues

    def __str__(self):
        return f"{self.title} by {self.author}"
