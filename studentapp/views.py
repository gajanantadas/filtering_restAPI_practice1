from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
#if i want to particular view then use this for django-filter import
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['city']
    filterset_fields = ['name','city']
    #filterset_fields = ['city']
    #without using django_filter
    """def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)"""


