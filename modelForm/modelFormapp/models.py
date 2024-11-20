from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=20,default='FirstName',verbose_name="Name",unique=True)
    lastname=models.CharField(max_length=20,verbose_name='Surname',blank=True)
    address=models.CharField(max_length=50)
    phnno=models.BigIntegerField(default=0,verbose_name="Phone Number")



    def __str__(self):
        return self.firstname
    
    class Meta:
        db_table="modelFormapp_Customer"