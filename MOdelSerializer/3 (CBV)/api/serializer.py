from rest_framework import serializers
from .models import Student

# Validator

class StudentSerializer(serializers.ModelSerializer):
	# Validators
	def start_with_s(value):
		if value[0].lower() != 's':
			raise serializers.ValidationError('Name should be start with S')
	name = serializers.CharField(validators = [start_with_s])
	class Meta:
		model = Student
		fields = ['name','rollno','city']

	
	#Field level validation (When Posting the Data)
	def validate_rollno(self,value):
		if value >= 200:
			raise serializers.ValidationError('Seats are full')
		return value
		
	#Object level validataion (When Posting the Data)
	def validate(self,data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'suresh' and ct.lower() != 'nad':
			raise serializers.ValidationError('City must be Nad')
		return data			