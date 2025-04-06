from rest_framework import generics, mixins
from .models import Student, Subject, Enrollment
from .serializers import StudentSerializer, SubjectSerializer, EnrollmentSerializer



class StudentAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id=id)
        else:
            return self.list(request)

    
    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id=id)
    
    def delete(self, request, id=id):
        return self.destroy(request, id=id)
    

class SubjectAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id=id)
        else:
            return self.list(request)
        
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id=id)
    
    def delete(self, request, id=id):
        return self.destroy(request, id=id)
    

class EnrollmentAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id=id)
        else:
            return self.list(request)
        
    
    def post(self, request):
        return self.create(request)
    
    def put(self,request, id=None):
        return self.update(request, id=id)
    
    def delete(self, request, id=id):
        return self.destroy(request, id=id)
    


