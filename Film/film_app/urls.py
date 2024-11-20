from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
   
   path('upcoming/', views.upcoming_movies, name='upcoming'),
   path('movie_list/', views.movie_list, name='movie_list'),
   path('select_showtime/<int:movie_id>/', views.select_showtime, name='select_showtime'),
   path('select_seat/<int:showtime_id>/', views.select_seat, name='select_seat'),

]