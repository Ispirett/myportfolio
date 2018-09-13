from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):

    my_jobs = Job.objects
    return render(request, 'jobs/index.html', {'my_jobs': my_jobs})


def about(request):

    my_jobs = Job.objects
    return render(request, 'jobs/about.html', {'my_jobs': my_jobs})