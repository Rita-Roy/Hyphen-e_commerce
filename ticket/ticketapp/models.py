from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator  #need to import the validators

# Create your models here.
class Movie(models.Model):  #stores movie information
    title=models.CharField(max_length=80, unique=True)
    genre=models.CharField(max_length=40)
    duration=models.IntegerField()
    release_date=models.DateField()
    ratings=models.DecimalField( 
        max_digits=3, #eg:1.5,2,2.0
        decimal_places=1,
        null=True, #not neccessary that the movie should have rating
        blank=True, #no probs if this field is empty
        validators=[MinValueValidator(1),MaxValueValidator(10)]  #to ensure that the rating is from 1 to 10
                                )
    class Meta:
        ordering=['-release_date'] #latest first
        verbose_name='Film'
        verbose_name_plural='Films'



    def __str__(self):
        return f"{self.title} (Rating: {self.ratings})"
    




class ShowTime(models.Model):  #scheduling the showtimie for each movie
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)  #foreignkey is used to establish relationship with the Movie
    date=models.DateField()
    time=models.TimeField()


    class Meta:
        ordering = ['date','time']
        verbose_name='Showtime'
        verbose_name_plural='Showtimes'

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"   #movie.title is used because it clearly indicates that u r accessing the title of the associated movie 
    



class Seat(models.Model): #managing seat availability for each showtime
    showtime=models.ForeignKey(ShowTime, on_delete=models.CASCADE) #as each seat is associated with the showtime we book seat based on the showtime(time and date)
    seat_number=models.CharField(max_length=5)  #charfield=alphanumeric so eg:A1,B2 eltc
    status=models.CharField(max_length=10, choices=[('available', 'Available'), ('booked', 'Booked')]) #it is in a tuple format 1st is tored in database,2nd is human readable displayed in forms and interface
    

    class Meta:
        ordering = ['seat_number']
        verbose_name= 'Seat'
        verbose_name_plural='Seats'
        unique_together=(('showtime', 'seat_number'),) #ensures unique seat number for each showtime

    def __str__(self):
        return f"{self.seat_number} - {self.status}"
    

