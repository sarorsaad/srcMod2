from django.shortcuts import render
from .forms import PatientForm, TestRequestForm

def my_view(request):
    patient_form = PatientForm()
    test_request_form = TestRequestForm()
    context = {
        'patient_form': patient_form,
        'test_request_form': test_request_form
    }
    return render(request, 'radio/my_template.html', context)
