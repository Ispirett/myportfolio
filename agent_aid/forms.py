from django import forms
from .models import ClientsDatabase

class ClientForm (forms.ModelForm):
    class Meta:
        model = ClientsDatabase
        fields = '__all__'
        widgets = { 'NAME' :forms.TextInput(attrs={'class': 'form-control'}),
                    'CONTACT' :forms.TextInput(attrs={'class': 'form-control'}),
                    'OCCUPATION': forms.TextInput(attrs={'class': 'form-control'}),
                    'CLIENT_NO': forms.NumberInput(attrs={'class': 'form-control'}),
                    'POLICY_NO ': forms.NumberInput(attrs={'class': 'form-control'}),
                    'POLICY_TYPE': forms.TextInput(attrs={'class ': 'form-control'}),
                    'POLICY_PROPERTIES': forms.TextInput(attrs={'class': 'form-control'}),
                    'ISSUE_DATE ': forms.DateInput(attrs={'class': 'form-control'}),
                    'REVIEW_DATE': forms.DateInput(attrs={'class': 'form-control'}),
                    'DOB ': forms.DateInput(attrs={'class': 'form-control'}),
                    'ADDRESS': forms.TextInput(attrs={'class': 'form-control'}),
                    'PREMIUM_AMOUNT': forms.TextInput(attrs={'class': 'form-control'}),
                    'MODE_OF_PAYMENT': forms.TextInput(attrs={'class': 'form-control'}),
                    'PDF ': forms.TextInput(attrs={'class':'btn btn-success btn-lg btn-block'}),
                  }