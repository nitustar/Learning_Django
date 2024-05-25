from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(50)])
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    # def clean_name(self):
    #     inputname = self.cleaned_data['name']
    #     print("Validating Name.")
    #     if len(inputname) < 4 :
    #         raise forms.ValidationError("The Minimum no of characters in the name field should be 4.")
    #     return inputname
    
    # def clean_rollno(self):
    #     inputrollno = self.cleaned_data['rollno']
    #     print("Validating Rollno Field")
    #     return inputrollno
    
    # def clean_email(self):
    #     inputemail = self.cleaned_data['email']
    #     print("Validating Email Field")
    #     return inputemail
    
    # def clean_feedback(self):
    #     inputfeedback = self.cleaned_data['feedback']
    #     print("Validating Feedback Field")
    #     return inputfeedback

    def clean(self):
        print("Toal Form Validation in single method")
        total_cleaned_data = super().clean()
        inputrollno = total_cleaned_data['rollno']
        if inputrollno <= 0:
            raise forms.ValidationError("The Rollno should be greater than zero.")
        

class SignupForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput)

    def clean(self):
        print("Validating the form")
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("Both passwords must be same.")
        
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Request from BOT... cannot be submitted.")