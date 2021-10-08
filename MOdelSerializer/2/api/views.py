from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def student_api(request):

	# Get method
	if request.method == 'GET':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)

		id = pythondata.get('id',None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data, content_type='application/json')

		student = Student.objects.all()
		serializer = StudentSerializer(student,many=True)			
		json_data = JSONRenderer().render(serializer.data)
		return HttpResponse(json_data, content_type='application/json')

	# Post method
	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg':'Data Created successfully'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data,content_type="application/json")
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type="application/json")

	# Update method
	if request.method == "PUT":
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id = id)
		serializer = StudentSerializer(stu,data=pythondata,partial=True) #For updating only specific data we use "partial=True" 
		if serializer.is_valid():
			serializer.save()
			res = {'msg':'Data Updated !!'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type="application/json")
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data, content_type="application/json")

	# Delete method
	if request.method == 'DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'msg':'Data deleted !!'}
		# json_data = JSONRenderer().render(res)
		# return HttpResponse(json_data, content_type="application/json")
		return JsonResponse(res, safe=False)