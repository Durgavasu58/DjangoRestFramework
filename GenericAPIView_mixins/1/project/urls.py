
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentList.as_view(),name='std'),
    path('studentapic/',views.StudentCreate.as_view()),
     path('studentapir/<int:pk>/',views.StudentRetreive.as_view()),
     path('studentapiu/<int:pk>/',views.StudentUpdate.as_view()),
     path('studentapid/<int:pk>/',views.StudentDelete.as_view()),
    # path('studentapi/<int:pk>/',views.StudentAPI.as_view(),name='std')
    
]
