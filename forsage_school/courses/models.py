from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class MyModel(models.Model):
    my_field = models.DateTimeField(default=datetime(2023, 1, 1))

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.IntegerField()  

    def __str__(self):
        return self.title
    



class Question(models.Model):
    image = models.URLField(max_length=255, default='default_image.jpg')
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')])

    def __str__(self):
        return self.text    
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    answered_questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.user.username
    



    
    


