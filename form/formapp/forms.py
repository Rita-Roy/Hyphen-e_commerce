from django import forms

class MyForm(forms.Form):    #forms-module name,Form-parent class ,MyForm-child class
    name=forms.CharField(max_length=20)  #char field can store upto 255 chara,TextField- more than 255
    address=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phoneno=forms.RegexField(regex=r'^\d{10}$')   #^-starts with,d-digits upto 10,$-ends with