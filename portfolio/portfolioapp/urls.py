from django.urls import path
from portfolioapp import views

urlpatterns=[
    path('',views.home),
    path("portfolio_mine",views.my_portfolio)
]