from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse



# def student_detail(request):
# 	stu = Student.objects.get(id=1)
# 	serializer = StudentSerializer(stu)
# 	json_data = JSONRenderer().render(serializer.data)
# 	return HttpResponse(json_data,content_type='application/json')


def student_detail(request):
	stu = Student.objects.get(id=2)
	serializer = StudentSerializer(stu)
	return JsonResponse(serializer.data)

def student_list(request):
	st1 = Student.objects.all()
	serializer = StudentSerializer(st1,many=True)
	return JsonResponse(serializer.data,safe=False)