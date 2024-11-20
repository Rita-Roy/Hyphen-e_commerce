from django.shortcuts import render, redirect
from .forms import PersonalInfoForm,EducationForm,WorkExperienceForm,SkillForm,ProjectForm
from .models import PersonalInfo,Education,WorkExperience,Skill,Project


def home(request):
    return render(request,'home.html')


#handles creating personal information
def create_personal_info(request):
    if request.method=="POST": #IF THE FORM IS SUBMITTED
        form=PersonalInfoForm(request.POST)
        if form.is_valid(): #data is validated and if it is valid
            form.save() #info is saved
            return redirect('add_education') #and redirected to this
        else: #if it is get
            form=PersonalInfoForm() #empty form is displayed
        return render(request,'personal_info_form.html',{'form':form})
    

#allows users to add thie education
def add_education(request,personal_info_id): #id is used to make sure that the particular user's education is going to add
    personal_info=PersonalInfo.objects.get(id=personal_info_id)
    if request.method=='POST':
        form=EducationForm(request.POST)
        if form.is_valid():
            education=form.save(commit=False)
            education.personal_info=personal_info
            education.save()
            return redirect('add_work_experience')
    else:
        form=EducationForm()
    return render(request,'education_form.html',{'form':form,"personal_info":personal_info})


def add_work_experience(request,personal_info_id): #id is used to make sure that the particular user's education is going to add
    personal_info=PersonalInfo.objects.get(id=personal_info_id)
    if request.method=='POST':
        form=WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience=form.save(commit=False)
            work_experience.personal_info=personal_info
            work_experience.save()
            return redirect('add_skills')
    else:
        form=EducationForm()
    return render(request,'work_experience_form.html',{'form':form,"personal_info":personal_info})



def add_skills(request,personal_info_id): #id is used to make sure that the particular user's education is going to add
    personal_info=PersonalInfo.objects.get(id=personal_info_id)
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.personal_info=personal_info
            skill.save()
            return redirect('add_project')
    else:
        form=SkillForm()
    return render(request,'skill_form.html',{'form':form,"personal_info":personal_info})


def add_project(request,personal_info_id): #id is used to make sure that the particular user's education is going to add
    personal_info=PersonalInfo.objects.get(id=personal_info_id)
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.personal_info=personal_info
            project.save()
            return redirect('resume_detail')
    else:
        form=ProjectForm()
    return render(request,'project_form.html',{'form':form,"personal_info":personal_info})


def resume_view(request,personal_info_id):
    personal_info=PersonalInfo.objects.get(id=personal_info_id)
    return render(request,'resume_detail.html',{'personal_info':personal_info})