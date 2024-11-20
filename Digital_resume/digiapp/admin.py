from django.contrib import admin
from .models import PersonalInfo, Education, WorkExperience, Skill, Project

# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Project)