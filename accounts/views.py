from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':

        form = RegisterationForm(request.POST)
        if form.is_valid():
            print('is valide')
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/products/')
    else:
        form = RegisterationForm()
        print('is not valide')
    context = {'form': form}
    return render(request, 'registration/singup.html', context)


@login_required(login_url='/accounts/login')
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}

    return render(request, 'profile.html', context)
