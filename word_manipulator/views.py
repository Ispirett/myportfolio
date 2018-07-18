from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import os
from word_manipulator.word_replace import ReplaceWord
from .forms import DocumentForm
from .models import Userfile
from.file_handeler import handle_uploaded_file
from  .word_replace import ReplaceWord
from  django.http import HttpResponseRedirect
#Create your views here.

def word_change(request):




    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.save()




            #return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'word_manipulator/wordmanipulator.html', {'form': form })


def change_word (request) :
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.save()

    users = Userfile.objects




    return render(request,'word_manipulator/changeword.html',{'users':users})


