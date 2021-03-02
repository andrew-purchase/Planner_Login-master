from django.shortcuts import render
from .models import Courses


# Create your views here.
def plan(request):
    cs = Courses.objects.all()
    return render(request, 'planner/planner.html', {'cs': cs})
