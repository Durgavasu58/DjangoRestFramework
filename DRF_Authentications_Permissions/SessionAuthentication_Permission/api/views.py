
from .models import Student
from .serializer import StudentSerializer
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly



# Check the settings file the restframework global settings are included

    

# use when local authentications are to be made & check settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated] # Open the url incognito broser u can login with username and password
    permission_classes = [AllowAny]
    permission_classes = [IsAdminUser] # Whehter user is not having staff user access  
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]