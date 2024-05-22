from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        inputname = self.cleaned_data['name']
        print("Validating Name.")
        if len(inputname) < 4 :
            raise forms.ValidationError("The Minimum no of characters in the name field should be 4.")
        return inputname
    
    def clean_rollno(self):
        inputrollno = self.cleaned_data['rollno']
        print("Validating Rollno Field")
        return inputrollno
    
    def clean_email(self):
        inputemail = self.cleaned_data['email']
        print("Validating Email Field")
        return inputemail
    
    def clean_feedback(self):
        inputfeedback = self.cleaned_data['feedback']
        print("Validating Feedback Field")
        return inputfeedback