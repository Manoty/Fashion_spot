from django.contrib.auth.forms import UserCreationForm
from django import forms
from auth.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account  # Use your custom Account model here
        fields = ['username', 'email', 'password1', 'password2']

class AccountUpdateForm(forms.ModelForm):  # Fix: Change 'Model' to 'ModelForm'
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):  # Fix: Adjust indentation
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
