from django.db import models
from django.contrib.auth.models import User

HAIRSTYLE_TYPE_CHOICES = [
    ('men', 'Men'),
    ('women', 'Women'),
    ('hair_coloring', 'Hair Coloring'),
    ('hair_treatment', 'Hair Treatment'),
]

class Hairstylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    specialization = models.CharField(max_length=100)  # e.g., "Hair Coloring Specialist"

    def __str__(self):
        return self.name

class Hairstyle(models.Model):
    images=models.ImageField(upload_to='images',default=None,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_minutes = models.IntegerField()
    hairstyle_type = models.CharField(max_length=15, choices=HAIRSTYLE_TYPE_CHOICES)
    created_by = models.ForeignKey(Hairstylist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_hairstyle_type_display()})"

class Appointment(models.Model):
    customer = models.CharField(max_length=20)
    stylist = models.ForeignKey(Hairstylist, on_delete=models.CASCADE)
    hairstyle = models.ForeignKey(Hairstyle, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.customer} with {self.stylist} on {self.appointment_date}"


