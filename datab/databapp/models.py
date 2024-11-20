from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    age=models.IntegerField()
    image=models.ImageField(upload_to='images',default=None,null=True)

    def __str__(self):  #str tells django what to print
        return self.name
    

    class Meta:   #build in class name, we are defining a class within another class for adding additional info
        db_table='databapp_employee'  #appname_classname

# Create your models here.





















#python manage.py makemigrations  #for class creation,changes in the class
#python manage.py migrate  #to save changes in the table
#this commands are executed to save the changes