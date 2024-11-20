from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=50,unique=True)
    status=[
        ('not_completed','Not Completed'),
        ('completed', "Completed"),
        ('on_going', 'On going')
    ]
    completion_status=models.CharField(
        max_length=15,
        choices=status,
        default='not_completed'
    )
    due_date=models.DateField()

    def __str__(self):
        return f"{self.task_name} - {self.get_completion_status()- {self.due_date}}"