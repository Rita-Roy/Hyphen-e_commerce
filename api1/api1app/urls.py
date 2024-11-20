from django.urls import path
from .import views


urlpatterns=[
    path('',views.api_overview),
    path('product-create/',views.Createproduct,name='product-create'),
    path('product-list/',views.showall,name='product-list'),
    path('singleproductview/<int:pk>/',views.singleprodview,name="singleproductview"),
    path('partialupdate/<int:pk>/',views.Updateproductpartial,name="partialupdate"),
    path('deleteproduct/<int:pk>/',views.Deleteproduct,name="deleteproduct")

]