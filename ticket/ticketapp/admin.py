from django.contrib import admin
from .models import Movie, ShowTime, Seat

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','duration','release_date','ratings',)  # Fields to display in the list view
    search_fields = ('title',)  # Add a search bar for titles

class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ('id','movie', 'date', 'time')  # Customize as per your ShowTime fields
    list_filter = ('movie', 'date',)  # Add filters for the movie and date fields

class SeatAdmin(admin.ModelAdmin):
    list_display = ('id','seat_number', 'status', 'showtime')  # Fields to display in the list view
    list_filter = ('status', 'showtime',)  # Add filters for status and showtime fields



# Register your models with the custom admin classes
admin.site.register(Movie, MovieAdmin)
admin.site.register(ShowTime, ShowTimeAdmin)
admin.site.register(Seat,SeatAdmin)



# Register your models here.
