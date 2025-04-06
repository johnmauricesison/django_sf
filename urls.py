from django.urls import path
from .views import StudentAPIView, GradeAPIView

urlpatterns = [
    path('student/', StudentAPIView.as_view(), name='student'),
    path('student/<int:id>/', StudentAPIView.as_view(), name='student'),
    path('grade/', GradeAPIView.as_view(), name='grade'),
    path('grade/<int:id>/', GradeAPIView.as_view(), name='grade'),
]