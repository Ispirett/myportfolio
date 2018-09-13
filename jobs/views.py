from django.shortcuts import render,redirect
from .models import Job
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    my_jobs = Job.objects
    return render(request, 'jobs/index.html', {'my_jobs': my_jobs})
""" if request.method == "POST":
        if request.POST['name'] and request.POST['subject'] and request.POST['email'] and request.POST['message']:
        name = request.POST['name']
        subject= request.POST['subject']
        email_from = settings.EMAIL_HOST_USER
        email_reciever = request.POST['email']
        message = request.POST['message']
        send_mail(subject, message, email_from, email_reciever,fail_silently=True)
        return redirect('homejobs') """



def about(request):

    my_jobs = Job.objects
    return render(request, 'jobs/about.html', {'my_jobs': my_jobs})