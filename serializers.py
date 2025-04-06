from rest_framework import serializers
from .models import Student, Subject, Enrollment

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True)
    
    total_tuition_fee = serializers.SerializerMethodField()
    discounted_tuition_fee = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()


    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'subjects', 'date_enrolled', 'mode_of_payment', 'total_tuition_fee', 'discounted_tuition_fee', 'discount']

    def get_total_tuition_fee(self, obj):
        return obj.total_tuition_fee()
    
    def get_discounted_tuition_fee(self,obj):
        return obj.discounted_tuition_fee()


    def discount(self, obj):
        return obj.final()
    
