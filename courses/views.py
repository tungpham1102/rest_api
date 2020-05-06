from django.shortcuts import render
from .serializers import CourseSerializer
from rest_framework import viewsets
from .models import Course

# Create your views here.


def index(request):
    return render(request, 'index.html')


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer