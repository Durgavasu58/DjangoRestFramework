
from .models import Student
from .serializer import StudentSerializer
from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



# Check the settings file the restframework global settings are included

    

# use when local authentications are to be made & check settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication] # Open the url incognito broser u can login with username and password
    permission_classes = [IsAuthenticated]