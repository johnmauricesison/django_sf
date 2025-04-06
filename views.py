from django.shortcuts import render

# Create your views here.

from rest_framework import generics, mixins
from .models import Student, Grade
from .serializers import StudentSerializer, GradeSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request, id=id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


class GradeAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request, id=id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request, id)
    
    def put(self, request, id = None):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id)