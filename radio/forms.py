from django import forms
from .models import Patient, TestRequest
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class TestRequestForm(forms.ModelForm):
    class Meta:
        model = TestRequest
        exclude = ['patient']