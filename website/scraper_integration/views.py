from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


from .scraper.scraper import get_data


# Create your views here.

def main_page(request):
    return render(request, 'scraper_integration/base.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect("main_page")
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})