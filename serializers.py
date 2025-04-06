
from rest_framework import serializers
from .models import Student, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'student','subject', 'score']


class StudentSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    average_grade = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'grades', 'average_grade']


    def get_average_grade(self,obj):
        grades = obj.grades.all()
        if grades:
            return sum(grade.score for grade in grades) / grades.count()
        return 0.0

