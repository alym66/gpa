from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.SubjectList.as_view(), name=views.SubjectList.name),
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name=views.SubjectDetail.name),
    path('students/', views.StudentList.as_view(), name=views.StudentList.name),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name=views.StudentDetail.name),
    path('gpa/', views.GPAList.as_view(), name=views.GPAList.name),
    path('gpa/<int:pk>/', views.GPADetail.as_view(), name=views.GPADetail.name),
    path('$/', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]