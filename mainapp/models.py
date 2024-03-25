from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class classes(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length= 200, null=True)
    instructor = models.CharField(max_length= 100, null=True)
   
    def __str__(self):
        return self.title


class assignment(models.Model):
    class_associated = models.ForeignKey(classes, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    

    def __str__(self): 
        return self.title
    
    
class questions(models.Model):
    class_course = models.ForeignKey(classes, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(assignment, on_delete=models.CASCADE, null=True)
    Number = models.IntegerField(null=True)
    Description = models.TextField()
# can add images if requied in question

def __str__(self):
    return str(self.Number)