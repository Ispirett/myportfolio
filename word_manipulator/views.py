from django.shortcuts import render, redirect
import os
from word_manipulator.word_replace import ReplaceWord
from .forms import DocumentForm
from .models import Userfile
from  django.http import HttpResponse
#Create your views here.

def word_change(request):
    users = Userfile.objects



    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()




            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'word_manipulator/wordmanipulator.html', {'form': form })


def change_word (request) :
  # users = Userfile.objects
   user_old_word = request.POST.get('old_word')

   doc = request.POST.get('document', False)
   doc_read = os.open()







   return render(request,'word_manipulator/changeword.html', {'useroldword' : user_old_word}, {'doc': doc_read})