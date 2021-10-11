from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class Student(admin.ModelAdmin):
	list_display=['id','name','rollno','city']