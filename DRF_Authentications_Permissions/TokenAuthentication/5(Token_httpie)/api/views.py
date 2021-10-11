
from .models import Student
from .serializer import StudentSerializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

 
# use when local authentications are to be made & check settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] # Open the url incognito broser u can login with username and password
    permission_classes = [IsAuthenticatedOrReadOnly]
    