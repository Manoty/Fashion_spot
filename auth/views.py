from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import redirect


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully')
            return redirect('registration-url')
    else:
        form = RegistrationForm()



    return render(request, 'auth/register.html', {"form": form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import redirect



@login_required
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully')
            return redirect('registration-url')
    else:
        form = RegistrationForm()



    return render(request, 'auth/register.html', {"form": form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    # Assuming you have a user account associated with the request
    user_account = request.user.account  # Replace with the actual attribute that links the user to the account

    # You can also pass additional context data to your profile template
    context = {
        'user_account': user_account,
        # Add more context data as needed
    }

    return render(request, 'auth/profile.html', context)