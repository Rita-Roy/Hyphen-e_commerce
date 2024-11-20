from django.db import models

#this model stores the personal info of the user
class PersonalInfo(models.Model):  
    name=models.CharField(max_length=20)
    email=models.EmailField()
    summary=models.TextField() #to store the users career goals 

    def __str__(self):
        return self.name
    

#to store the users educational background
class Education(models.Model):
    personal_info=models.ForeignKey(PersonalInfo,related_name='education',on_delete=models.CASCADE)
    degree=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    year=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.degree} from {self.institution}"


#to store the work experience of the user
class WorkExperience(models.Model):
    personal_info=models.ForeignKey(PersonalInfo,related_name="work_experience",on_delete=models.CASCADE)
    title=models.CharField(max_length=100)#job title
    company=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} at {self.company}"
    

#to store the skills of the user
class Skill(models.Model):
    personal_info=models.ForeignKey(PersonalInfo, related_name="skills",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)#sskills

    def __str__(self):
        return self.name
    
#store the project details of the user
class Project(models.Model):
    personal_info=models.ForeignKey(PersonalInfo,related_name="project",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name
    
    
