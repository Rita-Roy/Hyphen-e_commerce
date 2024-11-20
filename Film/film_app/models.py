from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    images=models.ImageField(upload_to='images',default=None,null=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    duration = models.DurationField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.DateField()

    def _str_(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    

    def _str_(self):
        return f"{self.movie.title} - {self.show_date} {self.show_time}"

class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.seat_number} - {'Available' if self.is_available else 'Booked'}"
