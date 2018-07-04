from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):

    my_jobs = Job.objects
    return render(request, 'jobs/home.html', {'my_jobs': my_jobs})