from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class StudentList(ListAPIView,CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUD(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer