from django.urls import path
from . import views

app_name = 'scraper_integration'
urlpatterns=[
    path('', views.main_page, name='main_page'),
    path('registration', views.registration, name='registration'),
]