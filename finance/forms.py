from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from finance.models import Transaction

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class LoginForm(UserCreationForm):
#    # email = forms.EmailField()
#     class meta:
#         model = User
#         fields = ['username', 'password1']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user', 'title', 'amount', 'transaction_type', 'date', 'category']
