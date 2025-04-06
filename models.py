from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
        
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    subject = models.CharField(max_length=100)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.subject} ({self.score})"
    
