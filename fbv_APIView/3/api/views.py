from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None): # pk is added for individual data

    if request.method == 'GET':
        id = pk # pk is added
        #Getting the data by id
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        #Getting Sll the data if ther is no id 
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Compelete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partialy Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted '})