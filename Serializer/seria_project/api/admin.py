from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentDetail(admin.ModelAdmin):
	list_display = ['id','name','rollno','city']
