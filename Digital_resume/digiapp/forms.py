from django import forms
from .models import PersonalInfo,WorkExperience,Education,Skill,Project
#allows user to input their personal information 
class PersonalInfoForm(forms.ModelForm):
    class Meta:  #it defines which model to use
        model=PersonalInfo
        fields="__all__"

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields="__all__"

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model=WorkExperience
        fields="__all__"

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields="__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"