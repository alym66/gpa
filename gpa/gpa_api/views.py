from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    name = 'subject-list'


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    name = 'subject-detail'


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student-list'


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    name = 'student-detail'


class GPAList(generics.ListCreateAPIView):
    queryset = GPA.objects.all()
    serializer_class = GPASerializer
    name = 'gpa-list'


class GPADetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPA.objects.all()
    serializer_class = GPASerializer
    name = 'gpa-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'students': reverse(StudentList.name, request=request),
            'subjects': reverse(SubjectList.name, request=request),
            'gpa': reverse(GPAList.name, request=request)
            })





