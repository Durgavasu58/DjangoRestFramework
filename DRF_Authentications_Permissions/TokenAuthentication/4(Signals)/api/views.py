
from .models import Student
from .serializer import StudentSerializer
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# ===============================================================

# http POST http://127.0.0.1:8000/gettoken/ username="user" password="User@123"
#   -->   pip install httpie Check urls.py

# ===============================================================
 
# use when local authentications are to be made & check settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] # Open the url incognito broser u can login with username and password
    