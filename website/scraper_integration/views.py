from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


from .scraper.scraper import get_data


# Create your views here.

def main_page(request):
    return render(request, 'scraper_integration/main_page.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("scraper_integration:main_page"))
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})


def scraper(request):
    objs = []
    for i in get_data(1, 1, "zilina"):
        print(i)
        objs.append(i)
    return render(request, 'scraper_integration/scraping.html', {'objs': objs})