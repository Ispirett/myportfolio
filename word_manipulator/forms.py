from django import forms
from .models import Userfile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Userfile
        fields = ['old_word','new_word', 'document']
        widgets = {'old_word': forms.TextInput(attrs={'class': 'form-control'}),
                   'new_word': forms.TextInput(attrs={'class': 'form-control'}),
                   'document': forms.FileInput(attrs={'class': 'btn btn-success btn-lg btn-block'})
                   }