
from .models import Student
from .serializer import StudentSerializer
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .custompermissions import MyPermission

# Check the settings file the restframework global settings are included

    

# use when local authentications are to be made & check settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes =[MyPermission] # Custom permission are given
    