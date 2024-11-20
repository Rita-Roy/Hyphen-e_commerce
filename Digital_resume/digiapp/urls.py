from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('resume/',views.resume_view,name='resume_view'),
    path('add-personal-info/',views.create_personal_info,name='add_personal_info'),
    path('add-education/',views.add_education,name='add_education'),
    path('add-work-experience/',views.add_work_experience,name='add_work_experience'),
    path('add-skill/',views.add_skills,name='add_skill'),
    path('add-project/',views.add_project,name='add_project'),
]