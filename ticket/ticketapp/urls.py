from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('accounts/login/',views.loginview,name='login'),
    path('logout',views.logout_view),
    path('accounts/sign_up',views.sign_up,name="sign_up"),
    path('reset',views.reset_home,name='reset'),
    path('passwordreset',views.resetpassword),
    path('movies/', views.movie_list, name='movie_list'), # List of movies
    path('movies/<int:movie_id>/showtimes/', views.showtime_list, name='showtime_list'), # Showtimes for a specific movie
    path('seat_selection/<int:movie_id>/<int:showtime_id>/', views.seat_selection, name='seat_selection'), # Seat selection for a specific showtime
    
]
