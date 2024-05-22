from django.shortcuts import render
# from . import forms
from .forms import StudentForm

# Create your views here.

def studentinputview(request):
    sent = False
    # form = forms.StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form validation success and printing data.")
            print('Name: ', form.cleaned_data['name'])
            print('Marks:', form.cleaned_data['marks'])
            sent = True
    form = StudentForm()
    return render(request, 'testapp/input.html', {'form':form, 'sent':sent})
