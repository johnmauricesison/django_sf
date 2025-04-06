from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentAPIView.as_view(), name="student"),
    path("students/<int:id>/", views.StudentAPIView.as_view, name="student"),

    path("subjects/", views.SubjectAPIView.as_view(), name="subjects"),
    path("subjects/<int:id>", views.SubjectAPIView.as_view(), name="subjects"),

    path("enrollments/", views.EnrollmentAPIView.as_view(), name="enrollments"),
    path("enrollments/<int:id>", views.EnrollmentAPIView.as_view(), name="enrollments")
]
