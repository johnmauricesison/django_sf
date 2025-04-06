from django.utils import timezone
from decimal import Decimal
from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True, default="default")
    name = models.CharField(max_length=100, default="student_default")
    program = models.CharField(max_length=100, default="program_default")
    year_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.student_id})"
    

class Subject(models.Model):
    subject_code = models.CharField(max_length=10, unique=True, default="default")
    subject_name = models.CharField(max_length=100, default="subject_default")
    units = models.IntegerField(default=0)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    def __str__(self):
        return self.subject_name
    

class Enrollment(models.Model):
    PAYMENT_CHOICES = [('Cash', 'Cash'), ('Installment', 'Installment')]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, default="")
    subjects = models.ManyToManyField(Subject)
    date_enrolled = models.DateTimeField(default=timezone.now)
    mode_of_payment = models.CharField(max_length=15, choices=PAYMENT_CHOICES, default="Installment")

    def total_tuition_fee(self):
        total = sum(sub.units * sub.cost_per_unit for sub in self.subjects.all())
        return total

    def discounted_tuition_fee(self):
        total = self.total_tuition_fee()
        if self.mode_of_payment == 'Cash':
            return total * Decimal('0.9')
        return total


    def discount(self):
        total = self.total_tuition_fee()
        discount = self.discounted_tuition_fee()
        final_fee = total - discount
        return final_fee
    

    def __str__(self):
        return f"Enrollment: {self.student.name} - {self.date_enrolled}"