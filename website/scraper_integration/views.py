from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ScrapingArgsForm
from .models import TableInfo, ScrapedData, AnalysedData
from .custom_functions import meanD, minD, maxD, medianD

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

@login_required(login_url='login')
def scraper(request):
    if request.method == 'POST':
        form = ScrapingArgsForm(request.POST)
        if form.is_valid():
            data = get_data(form['buy_or_rent'].value(), form['type_of_property'].value(), form['location'].value())
            request.session['scraper_data'] = data
            return redirect(reverse('scraper_integration:results'))
    else:
        user = request.user
        length = TableInfo.objects.filter(owner=user).count()
        form = ScrapingArgsForm()
        return render(request, 'scraper_integration/scraping.html', {'form': form, 'length': length})

@login_required(login_url='login')
def view_tables(request):
    if request.method == "POST":
        table_id = request.POST.get('table-id')

        if table_id:
            table = TableInfo.objects.get(id=table_id)
            table.delete()

    user = request.user
    table_info = TableInfo.objects.filter(owner=user)
    analysed_table = AnalysedData.objects.filter(table__in=table_info)
    return render(request, 'scraper_integration/tables.html', {'analysed_table': analysed_table})

@login_required(login_url='login')
def results(request):
    data = request.session['scraper_data']
    del request.session['scraper_data']
    data_len = range(len(data['price']))
    user = request.user

    table = TableInfo(owner=user, name=data['location'][0])

    analysis = AnalysedData(
        table=table,

        avg_price = meanD(data['price']),
        avg_price_per_sqm = meanD(data['price_per_sq_m']),
        avg_sq_meter = meanD(data['sq_meter']),

        min_price = minD(data['price']),
        min_price_per_sqm = minD(data['price_per_sq_m']),
        min_sq_meter = minD(data['sq_meter']),

        max_price = maxD(data['price']),
        max_price_per_sqm = maxD(data['price_per_sq_m']),
        max_sq_meter = maxD(data['sq_meter']),

        median_price = medianD(data['price']),
        median_price_per_sqm = medianD(data['price_per_sq_m']),
        median_sq_meter = medianD(data['sq_meter']),
    )

    table.save()
    analysis.save()

    return render(request, 'scraper_integration/results.html', {'data': data, 'range': data_len})