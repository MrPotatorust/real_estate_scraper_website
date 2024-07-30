from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, ScrapingArgsForm
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
    if request.method == 'POST':
        form = ScrapingArgsForm(request.POST)
        if form.is_valid():
            data = get_data(form['buy_or_rent'].value(), form['type_of_property'].value(), form['location'].value())

            request.session['scraper_data'] = data
            return redirect(reverse('scraper_integration:results'))
    else:
        form = ScrapingArgsForm()
        return render(request, 'scraper_integration/scraping.html', {'form': form})
    

def results(request):
    data = request.session['scraper_data']
    del request.session['scraper_data']
    print(data['price'][2])
    data_len = range(len(data['price']))
    return render(request, 'scraper_integration/results.html', {'data': data, 'range': data_len})