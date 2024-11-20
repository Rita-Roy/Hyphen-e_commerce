from django.db import models

# Create your models here.
class Library(models.Model):
    title=models.CharField(max_length=20,verbose_name="Title",unique=True)
    author=models.CharField(max_length=20,verbose_name="Author")
    isbn=models.BigIntegerField(default=000,verbose_name="ISBN",unique=True)
    genre=models.CharField(max_length=20,verbose_name="Genre")


    def __str__(self):
        return self.title

    class Meta:
        db_table="libraryapp_Library"