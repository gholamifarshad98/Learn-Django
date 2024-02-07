from django.db import models

class Student(models.Model):
    TEACHER = (("ahmadi", "Ahmadi"),("abdi","Abdi"),("bahrami", "Bahrami"))
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    std_number = models.IntegerField()
    teacher = models.CharField(max_length = 25, choices = TEACHER)    
    
    
    
    
    