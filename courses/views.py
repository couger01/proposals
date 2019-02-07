from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

# Create your views here.

def index(request):
    return render(request, 'courses/index.html')


class CourseList(ListView):
    model = Course
