from django.shortcuts import render
from . import forms

# Create your views here.

def feedbackview(request):
    sent = False
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and Printing Information")
            print("Name: ", form.cleaned_data['name'])
            print("Roll No.: ", form.cleaned_data['rollno'])
            print("Email: ", form.cleaned_data['email'])
            print("FeedBack: ", form.cleaned_data['feedback'])
            sent = True
    form = forms.FeedBackForm()

    return render(request, "testapp/feedback.html", {'form':form, 'sent':sent})