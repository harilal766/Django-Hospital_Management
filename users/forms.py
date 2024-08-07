from django import forms
from allauth.account.forms import SignupForm
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)