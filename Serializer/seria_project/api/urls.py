
from django.urls import path
from .import views

urlpatterns = [
   path('',views.student_detail,name='stu'),
   path('list/',views.student_list,name='list')
]
