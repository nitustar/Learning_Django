from django.shortcuts import render
from .forms import FeedBackForm, SignupForm

# Create your views here.

def feedbackview(request):
    sent = False
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and Printing Information")
            print("Name: ", form.cleaned_data['name'])
            print("Roll No.: ", form.cleaned_data['rollno'])
            print("Email: ", form.cleaned_data['email'])
            print("FeedBack: ", form.cleaned_data['feedback'])
            sent = True
    form = FeedBackForm()
    return render(request, "testapp/feedback.html", {'form':form, 'sent':sent})

def signupview(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print("Form Validation Success and Printing Information")
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Password: ", form.cleaned_data['password'])
    return render(request, 'testapp/signup.html', {'form':form})
