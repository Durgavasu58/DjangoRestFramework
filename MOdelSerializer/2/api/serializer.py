from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	# name = serializers.CharField(read_only=True)# The Name will not be updated, we are restricting --1--
	class Meta:
		model = Student
		fields = ['id','name','rollno','city']
		# read_only_fields = ['name','roll']#The Name,rollno will not be updated, we are restricting. Two ways u can do it --2--
		extra_kwargs = {'name':{'read_only':True}}