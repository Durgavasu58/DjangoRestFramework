from rest_framework import serializers
from .models import Student

# Validator
def start_with_s(value):
	if value[0].lower() != 's':
		raise serializers.ValidationError('Name should be start with S')

class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100, validators=[start_with_s])
	rollno = serializers.IntegerField()
	city = serializers.CharField(max_length=100) 

	def create(self,validated_data):
		return Student.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name',instance.name)
		instance.rollno = validated_data.get('rollno',instance.rollno)
		instance.city = validated_data.get('city',instance.city)
		instance.save()
		return instance

	#Field level validation
	def validate_rollno(self,value):
		if value >= 200:
			raise serializers.ValidationError('Seats are full')
		return value
		
	#Object level validataion
	def validate(self,data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'suresh' and ct.lower() != 'nad':
			raise serializers.ValidationError('City must be Nad')
		return data			