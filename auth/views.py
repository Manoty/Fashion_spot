from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Succesfully')
            return redirect('registration_url')

        else:
            form = RegistrationForm()
    return render(request, 'auth/register.html', {"form": form})
